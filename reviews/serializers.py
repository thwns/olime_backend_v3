from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    lovers_num = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = (
            "user",
            "kind",
            "payload",
            "rating",
            "rating_1",
            "rating_2",
            "rating_3",
            "rating_4",
            "rating_5",
            "lovers_num",
        )

    def get_lovers_num(self, review):
        return review.lovers_num()
