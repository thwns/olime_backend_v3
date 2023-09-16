from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
    OpenApiExample,
    inline_serializer
)
from drf_spectacular.types import OpenApiTypes
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task_Personal
from .serializers import Task_PersonalSerializer


class Task_PersonalView(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Task_PersonalSerializer,
        responses={201: Task_PersonalSerializer},
    )
    def get(self, request):
        all_Task_Personal = Task_Personal.objects.filter(user=request.user)
        serializer = Task_PersonalSerializer(
            all_Task_Personal,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=Task_PersonalSerializer,
        responses={201: Task_PersonalSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Task_PersonalSerializer(data=request.data)
            if serializer.is_valid():
                task_personal = serializer.save(
                    user=request.user,
                )
                serializer = Task_PersonalSerializer(task_personal)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class Task_PersonalDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task_Personal.objects.get(pk=pk)
        except Task_Personal.DoesNotExist:
            raise NotFound

    @extend_schema(
        responses={200: Task_PersonalSerializer},
    )
    def get(self, request, pk):
        task_personal = self.get_object(pk)
        serializer = Task_PersonalSerializer(task_personal)
        return Response(serializer.data)

    @extend_schema(
        request=Task_PersonalSerializer,
        responses={200: Task_PersonalSerializer},
    )
    def put(self, request, pk):
        task_personal = self.get_object(pk)
        serializer = Task_PersonalSerializer(task_personal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @extend_schema(
        responses={204: None},
    )
    def delete(self, request, pk):
        task_personal = self.get_object(pk)
        task_personal.delete()
        return Response(status=HTTP_204_NO_CONTENT)
