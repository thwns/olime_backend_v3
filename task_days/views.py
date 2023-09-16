from rest_framework import viewsets
from .models import Task_Day
from .serializers import Task_DaySerializer


class TaskDayViewSet(viewsets.ModelViewSet):
    queryset = Task_Day.objects.all()
    serializer_class = Task_DaySerializer


"""from drf_spectacular.utils import (
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
from django.db import transaction
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task_Day
from .serializers import Task_DaySerializer


class Task_Days(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def get(self, request):
        all_Task_Days = Task_Day.objects.all()
        serializer = Task_DaySerializer(
            all_Task_Days,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Task_DaySerializer(data=request.data)
            if serializer.is_valid():
                task_day = serializer.save()
                serializer = Task_DaySerializer(task_day)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


class Task_DayDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task_Day.objects.get(pk=pk)
        except Task_Day.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def get(self, request, pk):
        task_day = self.get_object(pk)
        serializer = Task_DaySerializer(
            task_day,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def delete(self, request, pk):
        task_day = self.get_object(pk)
        task_day.delete()
        return Response(status=HTTP_200_OK)

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def put(self, request, pk):
        task_day = self.get_object(pk)
        serializer = Task_DaySerializer(
            task_day,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            task_day = serializer.save()
            serializer = Task_DaySerializer(
                task_day,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)"""


'''class Task_Days(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def get(self, request):
        all_Task_Days = Task_Day.objects.filter(
            # Filtering task days where the user is in the list of users related to the task day
            user__in=[request.user.id]
        ).prefetch_related('difficult_question', 'user')  # Including 'user' in prefetch_related to optimize queries
        serializer = Task_DaySerializer(
            all_Task_Days,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Task_DaySerializer(data=request.data)
            if serializer.is_valid():
                with transaction.atomic():  # Start of atomic transaction block
                    # Removing the user parameter as the users will be handled through ManyToMany field in the serializer
                    task_day = serializer.save()
                    difficult_questions_pks = request.data.get(
                        "difficult_questions")
                    for difficult_question_pk in difficult_questions_pks:
                        difficult_question = Difficult_Question.objects.get(
                            pk=difficult_question_pk)
                        task_day.difficult_question.add(difficult_question)
                # End of atomic transaction block
                serializer = Task_DaySerializer(task_day)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


class Task_DayDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Task_Day.objects.get(pk=pk, user=user)
        except Task_Day.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def get(self, request, pk):
        task_day = self.get_object(pk, request.user)
        serializer = Task_DaySerializer(
            task_day,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def delete(self, request, pk):
        task_day = self.get_object(pk, request.user)
        task_day.delete()
        return Response(status=HTTP_200_OK)

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def put(self, request, pk):
        task_day = self.get_object(pk, request.user)
        serializer = Task_DaySerializer(
            task_day,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            task_day = serializer.save()
            serializer = Task_DaySerializer(
                task_day,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)'''
