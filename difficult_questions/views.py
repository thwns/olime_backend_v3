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
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from rest_framework.exceptions import NotFound, NotAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Difficult_Question
from .serializers import Difficult_QuestionSerializer


class Difficult_QuestionsView(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Difficult_QuestionSerializer,
        responses={201: Difficult_QuestionSerializer},
    )
    def get(self, request):
        all_questions = Difficult_Question.objects.all()
        serializer = Difficult_QuestionSerializer(
            all_questions, many=True, context={"request": request})
        return Response(serializer.data)

    @extend_schema(
        request=Difficult_QuestionSerializer,
        responses={201: Difficult_QuestionSerializer},
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Difficult_QuestionSerializer(data=request.data)
            if serializer.is_valid():
                question = serializer.save(user=request.user)
                serializer = Difficult_QuestionSerializer(question)
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class Difficult_QuestionDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Difficult_Question.objects.get(pk=pk)
        except Difficult_Question.DoesNotExist:
            raise NotFound

    @extend_schema(
        responses={200: Difficult_QuestionSerializer},
    )
    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = Difficult_QuestionSerializer(question)
        return Response(serializer.data)

    @extend_schema(
        request=Difficult_QuestionSerializer,
        responses={200: Difficult_QuestionSerializer},
    )
    def put(self, request, pk):
        question = self.get_object(pk)
        serializer = Difficult_QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @extend_schema(
        responses={204: None},
    )
    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=HTTP_204_NO_CONTENT)
