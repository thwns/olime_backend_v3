from rest_framework import serializers
from .models import Book, Lecture, Content, Track
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer
from followings.models import Following


class TrackListSerializer(serializers.ModelSerializer):

    leader = TinyUserSerializer(read_only=True)

    class Meta:
        model = Track
        fields = (
            "name",
            "image",
            "description",
            "leader",
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"


class TrackDetailSerializer(serializers.ModelSerializer):

    leader = TinyUserSerializer(read_only=True)
    category = CategorySerializer(
        read_only=True,
        many=True
    )
    rating = serializers.SerializerMethodField()
    is_leader = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()
    followers_num = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = (
            "leader",
            "category",
            "photos",
            "rating",
            "is_leader",
            "is_followed",
            "followers_num",
        )

    def get_rating(self, tracks):
        return tracks.rating()

    def get_is_leader(self, tracks):
        request = self.context["request"]
        return tracks.leader == request.user

    def get_is_followed(self, tracks):
        request = self.context["request"]
        return Following.objects.filter(
            user=request.user,
            track__pk=tracks.pk,
        ).exists()

    '''def get_followers_num(self, track):
        return track.followers_num()'''


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = "__all__"


class ContentDetailSerializer(serializers.ModelSerializer):

    leader = TinyUserSerializer(read_only=True)
    books = BookSerializer(
        read_only=True,
        many=True,
    )
    lectures = LectureSerializer(
        read_only=True,
        many=True,
    )
    tracks = TrackListSerializer(
        read_only=True,
        many=True
    )
    category = CategorySerializer(
        read_only=True,
        many=True
    )
    rating = serializers.SerializerMethodField()
    is_leader = serializers.SerializerMethodField()
    # is_followed = serializers.SerializerMethodField()
    # photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = (
            "leader",
            "books",
            "lectures",
            "category",
            "tracks",
            "rating",
            "is_leader",
            # "is_followed",
            # "photos",
        )

    def get_rating(self, content):
        return content.rating()

    def get_is_leader(self, content):
        request = self.context["request"]
        return content.leader == request.user

    '''def get_is_followed(self, track):
        request = self.context["request"]
        return Following.objects.filter(
            user=request.user,
            track__pk=track.pk,
        ).exists()'''


class ContentListSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_leader = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = (
            "pk",
            "name",
            "image",
            "types",
            "author",
            "company",
            "rating",
            "is_leader",
            "photos",
        )

    def get_rating(self, content):
        return content.rating()

    def get_is_leader(self, content):
        request = self.context.get("request")
        if request:
            return content.leader == request.user
        return False


class ContentShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = "__all__"
