from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from django.conf import settings
from rest_framework.views import APIView
from django.db import transaction
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.response import Response
from .models import Reply
from .serializers import ReplySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ReplyDetail(APIView):
    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=ReplySerializer,
        responses={201: ReplySerializer},
    )
    def put(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySerializer(
            reply, data=request.data, partial=True)
        if serializer.is_valid():
            updated_reply = serializer.save()
            return Response(
                ReplySerializer(updated_reply).data,
            )
        else:
            return Response(serializer.errors)

    @extend_schema(
        request=ReplySerializer,
        responses={201: ReplySerializer},
    )
    def delete(self, request, pk):
        reply = self.get_object(pk)
        reply.delete()
        return Response(status=HTTP_204_NO_CONTENT)
