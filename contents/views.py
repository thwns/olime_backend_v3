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
from .models import Book, Lecture, Content, Track
from categories.models import Category
from .serializers import (
    BookSerializer,
    LectureSerializer,
    ContentListSerializer,
    ContentDetailSerializer,
    ContentShowSerializer,
    TrackListSerializer,
    TrackSerializer,
    TrackDetailSerializer,
)
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


'''@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'tags',
                OpenApiTypes.STR,
                description='Comma separated list of tag IDs to filter',
            ),
            OpenApiParameter(
                'ingredients',
                OpenApiTypes.STR,
                description='Comma separated list of ingredient IDs to filter',
            ),
        ]
    )
)'''


class Books(APIView):
    @extend_schema(
        request=BookSerializer,
        responses={201: BookSerializer},
    )
    def get(self, request):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=BookSerializer,
        responses={201: BookSerializer},
    )
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

    @extend_schema(
        request=BookSerializer,
        responses={201: BookSerializer},
    )
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    @extend_schema(
        request=BookSerializer,
        responses={201: BookSerializer},
    )
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

    @extend_schema(
        request=BookSerializer,
        responses={201: BookSerializer},
    )
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Tracks(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        request=TrackListSerializer,
        responses={201: TrackListSerializer},
    )
    def get(self, request):
        all_tracks = Track.objects.all()
        serializer = TrackSerializer(all_tracks, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TrackSerializer,
        responses={201: TrackSerializer},
    )
    def post(self, request):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            track = serializer.save()
            return Response(TrackSerializer(track).data)
        else:
            return Response(serializer.errors)


class TrackDetail(APIView):
    def get_object(self, pk):
        try:
            return Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=TrackDetailSerializer,
        responses={201: TrackDetailSerializer},
    )
    def get(self, request, pk):
        track = self.get_object(pk)
        serializer = TrackDetailSerializer(track)
        return Response(serializer.data)

    @extend_schema(
        request=TrackDetailSerializer,
        responses={201: TrackDetailSerializer},
    )
    def put(self, request, pk):
        track = self.get_object(pk)
        serializer = TrackDetailSerializer(
            track,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_track = serializer.save()
            return Response(
                BookSerializer(updated_track).data,
            )
        else:
            return Response(serializer.errors)

    @extend_schema(
        request=TrackSerializer,
        responses={201: TrackSerializer},
    )
    def delete(self, request, pk):
        track = self.get_object(pk)
        track.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Lectures(APIView):
    @extend_schema(
        request=LectureSerializer,
        responses={201: LectureSerializer},
    )
    def get(self, request):
        all_lectures = Lecture.objects.all()
        serializer = LectureSerializer(all_lectures, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=LectureSerializer,
        responses={201: LectureSerializer},
    )
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

    @extend_schema(
        request=LectureSerializer,
        responses={201: LectureSerializer},
    )
    def get(self, request, pk):
        lecture = self.get_object(pk)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)

    @extend_schema(
        request=LectureSerializer,
        responses={201: LectureSerializer},
    )
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

    @extend_schema(
        request=LectureSerializer,
        responses={201: LectureSerializer},
    )
    def delete(self, request, pk):
        lecture = self.get_object(pk)
        lecture.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Contents(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        request=ContentListSerializer,
        responses={201: ContentListSerializer},
    )
    def get(self, request):
        all_contents = Content.objects.all()
        serializer = ContentListSerializer(
            all_contents,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=ContentShowSerializer,
        responses={201: ContentShowSerializer},
    )
    def post(self, request):
        serializer = ContentShowSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    content = serializer.save(leader=request.user)
                    tracks = request.data.get("tracks")
                    for track_pk in tracks:
                        track = Track.objects.get(pk=track_pk)
                        content.tracks.add(track)
                    books = request.data.get("books")
                    for book_pk in books:
                        book = Book.objects.get(pk=book_pk)
                        content.books.add(book)
                    categories = request.data.get("category")
                    for category_pk in categories:
                        category_temp = Category.objects.get(
                            pk=category_pk)
                        content.category.add(category_temp)
                    lectures = request.data.get("lectures")
                    for lecture_pk in lectures:
                        lecture = Lecture.objects.get(pk=lecture_pk)
                        content.lectures.add(lecture)
                    serializer = ContentShowSerializer(content)
                    return Response(serializer.data)
            except Exception:
                raise ParseError(
                    "Category or Book or Lecture or Track not found")

        else:
            return Response(serializer.errors)


class ContentDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=ContentDetailSerializer,
        responses={201: ContentDetailSerializer},
    )
    def get(self, request, pk):
        content = self.get_object(pk)
        serializer = ContentDetailSerializer(
            content,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=ContentDetailSerializer,
        responses={201: ContentDetailSerializer},
    )
    def put(self, request, pk):
        content = self.get_object(pk)
        if content.leader != request.user:
            raise PermissionDenied
        serializer = ContentDetailSerializer(
            content,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "books" in request.data:
                books = request.data.get("books")
                try:
                    with transaction.atomic():
                        content.books.clear()
                        for book_pk in books:
                            book = Book.objects.get(pk=book_pk)
                            content.books.add(book)
                except Exception:
                    raise ParseError("Book not found")

            if "category" in request.data:
                categories = request.data.get("category")
                try:
                    room.amenities.clear()
                    for category_pk in categories:
                        category_temp = Category.objects.get(pk=category_pk)
                        content.category.add(category_temp)
                except Exception:
                    raise ParseError("Category not found")

            if "lectures" in request.data:
                lectures = request.data.get("lectures")
                try:
                    content.lectures.clear()
                    for lecture_pk in lecture:
                        lecture = Lecture.objects.get(pk=lecture_pk)
                        content.lectures.add(lecture)
                except Exception:
                    raise ParseError("Lecture not found")

            if "tracks" in request.data:
                tracks = request.data.get("tracks")
                try:
                    content.tracks.clear()
                    for track_pk in track:
                        track = Track.objects.get(pk=track_pk)
                        content.tracks.add(track)
                except Exception:
                    raise ParseError("Track not found")

            updated_content = serializer.save()

            return Response(ContentDetailSerializer(updated_content).data)

        else:
            return Response(serializer.errors)

    @extend_schema(
        request=ContentDetailSerializer,
        responses={201: ContentDetailSerializer},
    )
    def delete(self, request, pk):
        content = self.get_object(pk)
        if content.leader != request.user:
            raise PermissionDenied
        content.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class ContentReviews(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
    )
    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        content = self.get_object(pk)
        serializer = ReviewSerializer(
            content.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    @extend_schema(
        request=ReviewSerializer,
        responses={201: ReviewSerializer},
    )
    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                content=self.get_object(pk),
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)


class ContentPhotos(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=PhotoSerializer,
        responses={201: PhotoSerializer},
    )
    def post(self, request, pk):
        content = self.get_object(pk)
        if request.user != content.leader:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(content=content)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


def make_error(request):
    division_by_zero = 1 / 0
