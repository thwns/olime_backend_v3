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
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TaskGuideline
from .serializers import TaskGuidelineSerializer


class TaskGuidelineListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: TaskGuidelineSerializer(many=True)},
    )
    def get(self, request):
        all_task_guidelines = TaskGuideline.objects.all()
        serializer = TaskGuidelineSerializer(
            all_task_guidelines, many=True, context={"request": request})
        return Response(serializer.data)

    @extend_schema(
        request=TaskGuidelineSerializer,
        responses={201: TaskGuidelineSerializer},
    )
    def post(self, request):
        serializer = TaskGuidelineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TaskGuidelineDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return TaskGuideline.objects.get(pk=pk)
        except TaskGuideline.DoesNotExist:
            raise NotFound

    @extend_schema(
        responses={200: TaskGuidelineSerializer},
    )
    def get(self, request, pk):
        task_guideline = self.get_object(pk)
        serializer = TaskGuidelineSerializer(
            task_guideline, context={"request": request})
        return Response(serializer.data)

    @extend_schema(
        responses={204: "No Content"},
    )
    def delete(self, request, pk):
        task_guideline = self.get_object(pk)
        task_guideline.delete()
        return Response(status=204)

    @extend_schema(
        request=TaskGuidelineSerializer,
        responses={200: TaskGuidelineSerializer},
    )
    def put(self, request, pk):
        task_guideline = self.get_object(pk)
        serializer = TaskGuidelineSerializer(
            task_guideline, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
