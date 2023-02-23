'''from drf_spectacular.utils import (
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
from .models import Review
from contents.models import content, track
from tasks.models import Task
from replys.models import Reply
from .serializers import (
    ReviewSerializer,
)
from replys.serializers import ReplySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Reviews(APIView):
    def get(self, request):
        all_reviews = Review.objects.all()
        serializer = ReviewSerializer(all_reviews, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                content_pk = request.data.get("content")
                if not track_pk:
                    raise ParseError("Track is required.")
                try:
                    track = Track.objects.get(pk=track_pk)
                except Track.DoesNotExist:
                    raise ParseError("Track not found")
                track_pk = request.data.get("track")
                if not track_pk:
                    raise ParseError("Track is required.")
                try:
                    track = Track.objects.get(pk=track_pk)
                except Track.DoesNotExist:
                    raise ParseError("Track not found")
                track_pk = request.data.get("track")
                if not track_pk:
                    raise ParseError("Track is required.")
                try:
                    track = Track.objects.get(pk=track_pk)
                except Track.DoesNotExist:
                    raise ParseError("Track not found")
                try:
                    with transaction.atomic():
                        task = serializer.save(
                            leader=request.user,
                            track=track,
                        )
                        serializer = TaskDetailSerializer(task)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Track not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class TaskDetail(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=TaskDetailSerializer,
        responses={201: TaskDetailSerializer},
    )
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)

    @extend_schema(
        request=TaskDetailSerializer,
        responses={201: TaskDetailSerializer},
    )
    def put(self, request, pk):
        task = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if task.leader != request.user:
            raise PermissionDenied

        serializer = TaskDetailSerializer(
            task,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "track" in request.data:
                track_pk = request.data.get("track")
                try:
                    track = Track.objects.get(pk=track_pk)
                    task.track = track
                except Track.DoesNotExist:  # 존재하지 않는 category id를 입력하면 에러 발생시킴
                    raise ParseError("Track not found")

            updated_task = serializer.save()

            return Response(TaskDetailSerializer(updated_task).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=TaskDetailSerializer,
        responses={201: TaskDetailSerializer},
    )
    def delete(self, request, pk):
        task = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if task.leader != request.user:
            raise PermissionDenied
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class ContentReviews(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
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
        content = self.get_object(pk)
        serializer = ReviewSerializer(
            content.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    @extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
    )
    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                content=self.get_object(pk),
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)'''
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
