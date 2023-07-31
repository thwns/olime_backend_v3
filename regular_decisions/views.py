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
from .models import Regular_Decision
from subjects.models import Subject
from .serializers import Regular_DecisionDetailSerializer


class Regular_Decisions(APIView):
    def get(self, request):
        all_regular_decisions = Regular_Decision.objects.all()
        serializer = Regular_DecisionDetailSerializer(
            all_regular_decisions, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=Regular_DecisionDetailSerializer,
        responses={201: Regular_DecisionDetailSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Regular_DecisionDetailSerializer(data=request.data)
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
                        regular_decision = serializer.save(
                            user=request.user,
                            subject=subject,
                        )
                        serializer = Regular_DecisionDetailSerializer(subject)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Subject not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class Regular_DecisionDetail(APIView):
    def get_object(self, pk):
        try:
            return Regular_Decision.objects.get(pk=pk)
        except Regular_Decision.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=Regular_DecisionDetailSerializer,
        responses={201: Regular_DecisionDetailSerializer},
    )
    def get(self, request, pk):
        regular_decision = self.get_object(pk)
        serializer = Regular_DecisionDetailSerializer(regular_decision)
        return Response(serializer.data)

    @extend_schema(
        request=Regular_DecisionDetailSerializer,
        responses={201: Regular_DecisionDetailSerializer},
    )
    def put(self, request, pk):
        regular_decision = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if regular_decision.user != request.user:
            raise PermissionDenied

        serializer = Regular_DecisionDetailSerializer(
            regular_decision,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "subject" in request.data:
                subject_pk = request.data.get("subject")
                try:
                    subject = Subject.objects.get(pk=subject_pk)
                    regular_decision.subject = subject
                except Subject.DoesNotExist:  # 존재하지 않는 category id를 입력하면 에러 발생시킴
                    raise ParseError("Subject not found")

            updated_regular_decision = serializer.save()

            return Response(Regular_DecisionDetailSerializer(updated_regular_decision).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=Regular_DecisionDetailSerializer,
        responses={201: Regular_DecisionDetailSerializer},
    )
    def delete(self, request, pk):
        regular_decision = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if regular_decision.user != request.user:
            raise PermissionDenied
        regular_decision.delete()
        return Response(status=HTTP_204_NO_CONTENT)
