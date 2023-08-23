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
from difficult_questions.models import Difficult_Question
from .models import Task_Day
from .serializers import Task_DaySerializer


class Task_Days(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Task_DaySerializer,
        responses={201: Task_DaySerializer},
    )
    def get(self, request):
        all_Task_Days = Task_Day.objects.filter(user=request.user)
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
                task_day = serializer.save(
                    user=request.user,
                )
                difficult_questions = request.data.get("difficult_questions")
                for difficult_question_pk in difficult_questions:
                    difficult_question = Difficult_Question.objects.get(
                        pk=difficult_question_pk)
                    task_day.difficult_questions.add(difficult_question)
                serializer = Task_DaySerializer(Task_Day)
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
        task_math = self.get_object(pk, request.user)
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
            return Response(serializer.errors)


"""class Workbooks(APIView):

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def get(self, request):
        all_workbooks = Workbook.objects.all()
        serializer = WorkbookSerializer(
            all_workbooks, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = WorkbookSerializer(data=request.data)
            if serializer.is_valid():
                workbook_evaluation_pk = request.data.get(
                    "workbook_evaluation")
                if not workbook_evaluation_pk:
                    raise ParseError("Workbook_Evaluation is required.")
                try:
                    workbook_evaluation = Workbook_Evaluation.objects.get(
                        pk=workbook_evaluation_pk)
                except Workbook_evaluation.DoesNotExist:
                    raise ParseError("Workbook_Evaluation not found")
                try:
                    with transaction.atomic():
                        workbook = serializer.save(
                            user=request.user,
                            workbook_evaluation=workbook_evaluation,
                        )
                        serializer = WorkbookSerializer(
                            workbook)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Workbook_Evaluation not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class WorkbookDetail(APIView):
    def get_object(self, pk):
        try:
            return Workbook.objects.get(pk=pk)
        except Workbook.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def get(self, request, pk):
        workbook = self.get_object(pk)
        serializer = WorkbookSerializer(workbook)
        return Response(serializer.data)

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def put(self, request, pk):
        workbook = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if workbook.user != request.user:
            raise PermissionDenied

        serializer = WorkbookSerializer(
            workbook,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "workbook_evaluations" in request.data:
                workbook_evaluations = request.data.get("workbook_evaluations")
                try:
                    workbook.workbooks_evaluations.clear()
                    for workbook_evaluation_pk in workbook_evaluations:
                        workbook_evaluation = Workbook_Evaluation.objects.get(
                            pk=workbook_evaluation_pk)
                        workbook.workbook_evaluations.add(workbook_evaluation)
                except Exception:
                    raise ParseError("Workbook_Evaluation not found")

            updated_workbook = serializer.save()

            return Response(WorkbookSerializer(updated_workbook).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def delete(self, request, pk):
        workbook = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if workbook.user != request.user:
            raise PermissionDenied
        workbook.delete()
        return Response(status=HTTP_204_NO_CONTENT)"""
