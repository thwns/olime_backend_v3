from rest_framework import serializers
from .models import User
from reviews.models import Review


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "name",
            "avatar",
            "username",
            "grade",
            "current_school",
            "target_school"
        )


class PrivateUserSerializer(serializers.ModelSerializer):

    my_reviews = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "pk",
            "login_path",
            "last_login",
            "username",
            "email",
            "date_joined",
            "avatar",
            "name",
            "is_host",
            "gender",
            "language",
            "my_reviews",
            "grade",
            "current_school",
            "target_school"
        )

    def get_my_reviews(self, user):
        request = self.context.get("request")
        if request:
            if user.is_authenticated:
                return Review.objects.filter(
                    user=request.user,
                ).values()
        return False
