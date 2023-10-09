from rest_framework import viewsets
from .models import Performance
from .serializers import PerformanceSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

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
from .models import Performance
from .serializers import PerformanceSerializer
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
            return Response(serializer.errors)


class Performances(APIView):

    @extend_schema(
        request=PerformanceSerializer,
        responses={201: PerformanceSerializer},
    )
    def get(self, request):
        all_performances = Performance.objects.all()
        serializer = PerformanceSerializer(all_performances, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=PerformanceSerializer,
        responses={201: PerformanceSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = PerformanceSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        performance = serializer.save(
                            user=request.user,
                            performance=performance,
                        )
                        serializer = PerformanceSerializer(performance)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Performance not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class PerformanceDetail(APIView):
    def get_object(self, pk):
        try:
            return Performance.objects.get(pk=pk)
        except Performance.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=PerformanceSerializer,
        responses={201: PerformanceSerializer},
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
        return Response(status=HTTP_204_NO_CONTENT)"""


class Performances(APIView):

    @extend_schema(
        request=PerformanceSerializer,
        responses={201: PerformanceSerializer},
    )
    def get(self, request):
        all_performances = Performance.objects.all()
        serializer = PerformanceSerializer(
            all_performances, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=PerformanceSerializer,
        responses={201: PerformanceSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = PerformanceSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        performance = serializer.save(
                            user=request.user,
                        )
                        serializer = PerformanceSerializer(
                            performance)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Performance not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class PerformanceDetail(APIView):
    def get_object(self, pk):
        try:
            return Performance.objects.get(pk=pk)
        except Performance.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=PerformanceSerializer,
        responses={201: PerformanceSerializer},
    )
    def get(self, request, pk):
        performance = self.get_object(pk)
        serializer = PerformanceSerializer(performance)
        return Response(serializer.data)

    @extend_schema(
        request=PerformanceSerializer,
        responses={201: PerformanceSerializer},
    )
    def put(self, request, pk):
        performance = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if performance.user != request.user:
            raise PermissionDenied

        serializer = PerformanceSerializer(
            performance,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            updated_performance = serializer.save()

            return Response(PerformanceSerializer(updated_performance).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=PerformanceSerializer,
        responses={201: PerformanceSerializer},
    )
    def delete(self, request, pk):
        performance = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if performance.user != request.user:
            raise PermissionDenied
        performance.delete()
        return Response(status=HTTP_204_NO_CONTENT)'''
