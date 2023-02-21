from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Reply


class ReplySerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    lovers_num = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = (
            "user",
            "payload",
            "lovers_num",
            "rating",
        )

    def get_lovers_num(self, reply):
        return reply.lovers_num()
