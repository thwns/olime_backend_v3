from rest_framework import serializers
from .models import Book, Lecture, Content, Track
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer


class TrackListSerializer(serializers.ModelSerializer):

    leader = TinyUserSerializer()

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
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = "__all__"

    def get_rating(self, content):
        return content.rating()

    def get_is_leader(self, content):
        request = self.context["request"]
        return content.leader == request.user


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
        request = self.context["request"]
        return content.leader == request.user
