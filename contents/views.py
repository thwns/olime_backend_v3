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
from .models import Book, Lecture, Content
from categories.models import Category
from .serializers import BookSerializer, LectureSerializer, ContentListSerializer, ContentDetailSerializer


class Books(APIView):

    def get(self, request):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(BookSerializer(book).data)
        else:
            return Response(serializer.errors)


class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(
            book,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_book = serializer.save()
            return Response(
                BookSerializer(updated_book).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Lectures(APIView):
    def get(self, request):
        all_lectures = Lecture.objects.all()
        serializer = LectureSerializer(all_lectures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            lecture = serializer.save()
            return Response(LectureSerializer(lecture).data)
        else:
            return Response(serializer.errors)


class LectureDetail(APIView):
    def get_object(self, pk):
        try:
            return Lecture.objects.get(pk=pk)
        except Lecture.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        lecture = self.get_object(pk)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)

    def put(self, request, pk):
        lecture = self.get_object(pk)
        serializer = LectureSerializer(
            lecture, data=request.data, partial=True)
        if serializer.is_valid():
            updated_lecture = serializer.save()
            return Response(
                LectureSerializer(updated_lecture).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        lecture = self.get_object(pk)
        lecture.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Contents(APIView):
    def get(self, request):
        all_contents = Content.objects.all()
        serializer = ContentListSerializer(all_contents, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = ContentDetailSerializer(data=request.data)
            if serializer.is_valid():
                content = serializer.save(leader=request.user)
                books = request.data.get("books")
                for book_pk in books:
                    try:
                        book = Book.objects.get(pk=book_pk)
                    except Book.DoesNotExist:
                        content.delete()
                        raise ParseError(f"Book with id {book_pk} not found")
                    content.books.add(book)
                lectures = request.data.get("lectures")
                for lecture_pk in lectures:
                    try:
                        lecture = Lecture.objects.get(pk=lecture_pk)
                    except Lecture.DoesNotExist:
                        content.delete()
                        raise ParseError(
                            f"Lecture with id {lecture_pk} not found")
                    content.lectures.add(lecture)
                tracks = request.data.get("tracks")
                for track_pk in tracks:
                    try:
                        track = Track.objects.get(pk=track_pk)
                    except Track.DoesNotExist:
                        content.delete()
                        raise ParseError(f"Track with id {track_pk} not found")
                    content.tracks.add(track)
                categories = request.data.get("categories")
                for category_pk in categories:
                    try:
                        category = Category.objects.get(pk=category_pk)
                    except Category.DoesNotExist:
                        content.delete()
                        raise ParseError(
                            f"Category with id {category_pk} not found")
                    content.categories.add(category)
                serializer = ContentDetailSerializer(content)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class ContentDetail(APIView):

    def get_object(self, pk):
        try:
            return Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        content = self.get_object(pk)
        serializer = ContentDetailSerializer(content)
        return Response(serializer.data)

    def put(self, request, pk):
        content = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if content.leader != request.user:
            raise PermissionDenied
         # your magic

    def delete(self, request, pk):
        content = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if content.leader != request.user:
            raise PermissionDenied
        content.delete()
        return Response(status=HTTP_204_NO_CONTENT)
