from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "name",
            "avatar",
            "username",
            "grade",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "pk",
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "grade",
        )
