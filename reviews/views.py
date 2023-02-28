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
from replys.models import Reply
from .models import Review
from replys.serializers import (
    ReplySerializer,
)
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ReviewReplys(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=ReplySerializer,
        responses={201: ReplySerializer},
    )
    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        review = self.get_object(pk)
        serializer = ReplySerializer(
            review.replys.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    @extend_schema(
        request=ReplySerializer,
        responses={201: ReplySerializer},
    )
    def post(self, request, pk):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            reply = serializer.save(
                user=request.user,
                review=self.get_object(pk),
            )
            serializer = ReplySerializer(reply)
            return Response(serializer.data)


class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise NotFound

    '''@extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
    )
    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)'''

    @extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
    )
    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(
            review, data=request.data, partial=True)
        if serializer.is_valid():
            updated_review = serializer.save()
            return Response(
                ReviewSerializer(updated_review).data,
            )
        else:
            return Response(serializer.errors)

    @extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
    )
    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=HTTP_204_NO_CONTENT)
