from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from .models import Task
from contents.models import Track
from .serializers import TaskListSerializer, TaskDetailSerializer


class Tasks(APIView):
    def get(self, request):
        all_tasks = Task.objects.all()
        serializer = TaskListSerializer(all_tasks, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TaskDetailSerializer,
        responses={201: TaskDetailSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = TaskDetailSerializer(data=request.data)
            if serializer.is_valid():
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
