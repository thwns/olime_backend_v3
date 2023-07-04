from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from workbook_evaluations.models import Workbook_Evaluation
from .models import Workbook
from .serializers import WorkbookSerializer


"""class Workbooks(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def get(self, request):
        all_Workbooks = Workbook.objects.filter(user=request.user)
        serializer = WorkbookSerializer(
            all_Workbooks,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def post(self, request):
        serializer = WorkbookSerializer(data=request.data)
        if serializer.is_valid():
            workbook = serializer.save(
                user=request.user,
            )
            workbook_evaluations = request.data.get("workbook_evaluations")
            for workbook_evaluation_pk in workbook_evaluations:
                workbook_evaluation = Workbook_Evaluation.objects.get(
                    pk=workbook_evaluation_pk)
                workbook.workbook_evaluations.add(workbook_evaluation)
            serializer = WorkbookSerializer(workbook)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WorkbookDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Workbook.objects.get(pk=pk, user=user)
        except Workbook.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def get(self, request, pk):
        workbook = self.get_object(pk, request.user)
        serializer = WorkbookSerializer(
            workbook,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def delete(self, request, pk):
        workbook = self.get_object(pk, request.user)
        workbook.delete()
        return Response(status=HTTP_200_OK)

    @extend_schema(
        request=WorkbookSerializer,
        responses={201: WorkbookSerializer},
    )
    def put(self, request, pk):
        workbook = self.get_object(pk, request.user)
        serializer = WorkbookSerializer(
            workbook,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            workbook = serializer.save()
            serializer = WorkbookSerializer(
                workbook,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)"""


class Workbooks(APIView):

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
                if not workbook_pk:
                    raise ParseError("Workbook_Evaluation is required.")
                try:
                    workbook_evaluation = Workbook_Evaluation.objects.get(
                        pk=workbook_evaluation_pk)
                except Workbook.DoesNotExist:
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
        return Response(status=HTTP_204_NO_CONTENT)
