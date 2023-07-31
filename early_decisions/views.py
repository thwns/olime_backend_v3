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
from .models import Early_Decision
from subjects.models import Subject
from .serializers import Early_DecisionDetailSerializer


class Early_Decisions(APIView):
    def get(self, request):
        all_early_decisions = Early_Decision.objects.all()
        serializer = Early_DecisionDetailSerializer(
            all_early_decisions, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=Early_DecisionDetailSerializer,
        responses={201: Early_DecisionDetailSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Early_DecisionDetailSerializer(data=request.data)
            if serializer.is_valid():
                subject_pk = request.data.get("subject")
                if not subject_pk:
                    raise ParseError("Subject is required.")
                try:
                    subject = Subject.objects.get(pk=subject_pk)
                except Subject.DoesNotExist:
                    raise ParseError("Subject not found")
                try:
                    with transaction.atomic():
                        early_decision = serializer.save(
                            user=request.user,
                            subject=subject,
                        )
                        serializer = Early_DecisionDetailSerializer(subject)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Subject not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class Early_DecisionDetail(APIView):
    def get_object(self, pk):
        try:
            return Early_Decision.objects.get(pk=pk)
        except Early_Decision.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=Early_DecisionDetailSerializer,
        responses={201: Early_DecisionDetailSerializer},
    )
    def get(self, request, pk):
        early_decision = self.get_object(pk)
        serializer = Early_DecisionDetailSerializer(early_decision)
        return Response(serializer.data)

    @extend_schema(
        request=Early_DecisionDetailSerializer,
        responses={201: Early_DecisionDetailSerializer},
    )
    def put(self, request, pk):
        early_decision = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if early_decision.user != request.user:
            raise PermissionDenied

        serializer = Early_DecisionDetailSerializer(
            early_decision,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "subject" in request.data:
                subject_pk = request.data.get("subject")
                try:
                    subject = Subject.objects.get(pk=subject_pk)
                    early_decision.subject = subject
                except Subject.DoesNotExist:  # 존재하지 않는 category id를 입력하면 에러 발생시킴
                    raise ParseError("Subject not found")

            updated_early_decision = serializer.save()

            return Response(Early_DecisionDetailSerializer(updated_early_decision).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=Early_DecisionDetailSerializer,
        responses={201: Early_DecisionDetailSerializer},
    )
    def delete(self, request, pk):
        early_decision = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if early_decision.user != request.user:
            raise PermissionDenied
        early_decision.delete()
        return Response(status=HTTP_204_NO_CONTENT)
