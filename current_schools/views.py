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
from .models import Current_School
from schools.models import School
from .serializers import Current_SchoolDetailSerializer


class Current_Schools(APIView):
    def get(self, request):
        all_current_schools = Current_School.objects.all()
        serializer = Current_SchoolDetailSerializer(
            all_current_schools, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=Current_SchoolDetailSerializer,
        responses={201: Current_SchoolDetailSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Current_SchoolDetailSerializer(data=request.data)
            if serializer.is_valid():
                school_pk = request.data.get("school")
                if not school_pk:
                    raise ParseError("School is required.")
                try:
                    school = School.objects.get(pk=school_pk)
                except School.DoesNotExist:
                    raise ParseError("School not found")
                try:
                    with transaction.atomic():
                        current_school = serializer.save(
                            user=request.user,
                            school=school,
                        )
                        serializer = Current_SchoolDetailSerializer(school)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("School not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class Current_SchoolDetail(APIView):
    def get_object(self, pk):
        try:
            return Current_School.objects.get(pk=pk)
        except Current_School.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=Current_SchoolDetailSerializer,
        responses={201: Current_SchoolDetailSerializer},
    )
    def get(self, request, pk):
        current_school = self.get_object(pk)
        serializer = Current_SchoolDetailSerializer(current_school)
        return Response(serializer.data)

    @extend_schema(
        request=Current_SchoolDetailSerializer,
        responses={201: Current_SchoolDetailSerializer},
    )
    def put(self, request, pk):
        current_school = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if current_school.user != request.user:
            raise PermissionDenied

        serializer = Current_SchoolDetailSerializer(
            current_school,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "school" in request.data:
                school_pk = request.data.get("school")
                try:
                    school = School.objects.get(pk=school_pk)
                    current_school.school = school
                except School.DoesNotExist:  # 존재하지 않는 category id를 입력하면 에러 발생시킴
                    raise ParseError("School not found")

            updated_current_school = serializer.save()

            return Response(Current_SchoolDetailSerializer(updated_current_school).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=Current_SchoolDetailSerializer,
        responses={201: Current_SchoolDetailSerializer},
    )
    def delete(self, request, pk):
        current_school = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if current_school.user != request.user:
            raise PermissionDenied
        current_school.delete()
        return Response(status=HTTP_204_NO_CONTENT)
