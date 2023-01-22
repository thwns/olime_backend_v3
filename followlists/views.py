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
from tasks.models import Task
from contents.models import Track
from .models import Followlist
from .serializers import (
    FollowlistDetailSerializer,
    FollowlistListSerializer,
)


class Followlists(APIView):

    @extend_schema(
        request=FollowlistListSerializer,
        responses={201: FollowlistListSerializer},
    )
    def get(self, request):
        all_followlists = Followlist.objects.all()
        serializer = FollowlistListSerializer(all_followlists, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=FollowlistDetailSerializer,
        responses={201: FollowlistDetailSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = FollowlistDetailSerializer(data=request.data)
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
                        followllist = serializer.save(
                            user=request.user,
                            track=track,
                        )
                        tasks = request.data.get("tasks")
                        for task_pk in tasks:
                            try:
                                task = Task.objects.get(pk=task_pk)
                            except Task.DoesNotExist:
                                followlist.delete()
                                raise ParseError(
                                    f"Task with id {task_pk} not found")
                            followlist.tasks.add(task)
                        serializer = FollowlistDetailSerializer(followlist)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Task not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class FollowlistDetail(APIView):
    def get_object(self, pk):
        try:
            return Followlist.objects.get(pk=pk)
        except Followlist.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=FollowlistDetailSerializer,
        responses={201: FollowlistDetailSerializer},
    )
    def get(self, request, pk):
        followlist = self.get_object(pk)
        serializer = FollowlistDetailSerializer(followlist)
        return Response(serializer.data)

    @extend_schema(
        request=FollowlistDetailSerializer,
        responses={201: FollowlistDetailSerializer},
    )
    def put(self, request, pk):
        followlist = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if followlist.user != request.user:
            raise PermissionDenied

        serializer = FollowlistDetailSerializer(
            followlist,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "tasks" in request.data:
                tasks = request.data.get("tasks")
                try:
                    followlist.tasks.clear()
                    for task_pk in tasks:
                        task = Task.objects.get(pk=task_pk)
                        followlist.tasks.add(task)
                except Exception:
                    raise ParseError("Task not found")

            if "track" in request.data:
                track_pk = request.data.get("track")
                try:
                    track = Track.objects.get(pk=track_pk)
                    followlist.track = track
                except Track.DoesNotExist:  # 존재하지 않는 track id를 입력하면 에러 발생시킴
                    raise ParseError("Track not found")

            updated_followlist = serializer.save()

            return Response(FollowlistDetailSerializer(updated_followlist).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=FollowlistDetailSerializer,
        responses={201: FollowlistDetailSerializer},
    )
    def delete(self, request, pk):
        task = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if task.leader != request.user:
            raise PermissionDenied
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)
