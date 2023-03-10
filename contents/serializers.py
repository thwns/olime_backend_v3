from rest_framework import serializers
from .models import Book, Lecture, Content, Track
from reviews.models import Review
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
    # is_leader = serializers.SerializerMethodField()
    # is_followed = serializers.SerializerMethodField()
    followers_num = serializers.SerializerMethodField()
    lovers_num = serializers.SerializerMethodField()
    # photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = (
            "leader",
            "category",
            "rating",
            # "is_leader",
            # "is_followed",
            "followers_num",
            "lovers_num",
        )

    def get_rating(self, tracks):
        return tracks.rating()

    '''def get_is_leader(self, tracks):
        request = self.context.get["request"]
        return tracks.leader == request.user

    def get_is_followed(self, tracks):
        request = self.context["request"]
        return Following.objects.filter(
            user=request.user,
            track__pk=tracks.pk,
        ).exists()'''

    def get_followers_num(self, track):
        return track.followers_num()

    def get_lovers_num(self, track):
        return track.lovers_num()


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
    # is_leader = serializers.SerializerMethodField()
    # is_followed = serializers.SerializerMethodField()
    # photos = PhotoSerializer(many=True, read_only=True)
    user_review = serializers.SerializerMethodField()
    lovers_num = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = (
            "pk",
            "content_parent",
            "leader",
            "books",
            "lectures",
            "category",
            "tracks",
            "rating",
            # "is_leader",
            # "photos",
            "lovers_num",
            "user_review",
        )

    def get_rating(self, content):
        return content.rating()

    '''def get_is_leader(self, content):
        request = self.context["request"]
        return content.leader == request.user'''

    def get_lovers_num(self, content):
        return content.lovers_num()

    '''def get_is_followed(self, track):
        request = self.context["request"]
        return Following.objects.filter(
            user=request.user,
            track__pk=track.pk,
        ).exists()'''

    def get_user_review(self, content):
        request = self.context.get("request")
        if request:
            if request.user.is_authenticated:
                return Review.objects.filter(
                    # user=request.user,
                    content_id=content.pk,
                ).values()
        return False


class ContentListSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_leader = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = (
            "pk",
            "content_parent",
            "name",
            "types",
            "author",
            "company",
            "rating",
            "is_leader",
            "image",
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
