from rest_framework.serializers import ModelSerializer
from .models import Book, Lecture, Content, Track
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class TrackListSerializer(ModelSerializer):

    leader = TinyUserSerializer()

    class Meta:
        model = Track
        fields = (
            "name",
            "image",
            "description",
            "leader",
        )


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = "__all__"


class ContentDetailSerializer(ModelSerializer):

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

    class Meta:
        model = Content
        fields = "__all__"


class ContentListSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = (
            "pk",
            "name",
            "image",
            "types",
            "author",
            "company",
        )
