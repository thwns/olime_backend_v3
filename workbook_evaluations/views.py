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
from .models import Workbook_Evaluation
from workbook_evaluations.serializers import (
    Workbook_EvaluationSerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly


"""class Workbook_Evaluations(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvaluationSerializer},
    )
    def get(self, request):
        all_Workbook_Evaluations = Workbook_Evaluation.objects.filter(
            user=request.user)
        serializer = Workbook_EvaluationSerializer(
            all_Workbook_Evaluations,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvaluationSerializer},
    )
    def post(self, request):
        serializer = Workbook_EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            workbook_evaluation = serializer.save(
                user=request.user,
            )
            serializer = Workbook_EvaluationSerializer(workbook_evaluation)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Workbook_EvaluationDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Workbook_Evaluation.objects.get(pk=pk, user=user)
        except Workbook_Evaluation.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvaluationSerializer},
    )
    def get(self, request, pk):
        workbook_evaluation = self.get_object(pk, request.user)
        serializer = Workbook_EvaluationSerializer(
            workbook_evalution,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvalutionSerializer},
    )
    def delete(self, request, pk):
        workbook_evalution = self.get_object(pk, request.user)
        workbook_evalution.delete()
        return Response(status=HTTP_200_OK)

    @extend_schema(
        request=Workbook_EvalutionSerializer,
        responses={201: Workbook_EvalutionSerializer},
    )
    def put(self, request, pk):
        workbook_evalution = self.get_object(pk, request.user)
        serializer = Workbook_EvalutionSerializer(
            workbook_evalution,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            workbook_evalution = serializer.save()
            serializer = Workbook_EvaluationSerializer(
                workbook_evalution,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)"""


class Workbook_Evaluations(APIView):

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvaluationSerializer},
    )
    def get(self, request):
        all_workbook_evaluations = Workbook_Evaluation.objects.all()
        serializer = Workbook_EvaluationSerializer(
            all_workbook_evaluations, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvaluationSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Workbook_EvaluationSerializer(data=request.data)
            if serializer.is_valid():
                workbook_pk = request.data.get("workbook")
                if not workbook_pk:
                    raise ParseError("Workbook is required.")
                try:
                    workbook = Workbook.objects.get(pk=workbook_pk)
                except Workbook.DoesNotExist:
                    raise ParseError("Workbook not found")
                try:
                    with transaction.atomic():
                        workbook_evaluation = serializer.save(
                            user=request.user,
                            workbook=workbook,
                        )
                        serializer = Workbook_EvaluationSerializer(
                            workbook_evaluation)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Workbook not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class Workbook_EvaluationDetail(APIView):
    def get_object(self, pk):
        try:
            return Workbook_Evaluation.objects.get(pk=pk)
        except Workbook_Evaluation.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvaluationSerializer},
    )
    def get(self, request, pk):
        workbook_evaluation = self.get_object(pk)
        serializer = Workbook_EvaluationSerializer(workbook_evaluation)
        return Response(serializer.data)

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvaluationSerializer},
    )
    def put(self, request, pk):
        workbook_evaluation = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if workbook_evaluation.user != request.user:
            raise PermissionDenied

        serializer = Workbook_EvaluationSerializer(
            workbook_evaluation,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "workbooks" in request.data:
                workbooks = request.data.get("workbooks")
                try:
                    workbook_evaluation.workbooks.clear()
                    for workbook_pk in workbooks:
                        workbook = Workbook.objects.get(pk=workbook_pk)
                        workbook_evaluation.workbooks.add(workbook)
                except Exception:
                    raise ParseError("Workbook not found")

            updated_workbook_evaluation = serializer.save()

            return Response(Workbook_EvaluationSerializer(updated_workbook_evaluation).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=Workbook_EvaluationSerializer,
        responses={201: Workbook_EvaluationSerializer},
    )
    def delete(self, request, pk):
        workbook_evaluation = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if workbook_evaluation.user != request.user:
            raise PermissionDenied
        workbook_evaluation.delete()
        return Response(status=HTTP_204_NO_CONTENT)
