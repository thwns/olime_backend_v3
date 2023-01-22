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
from contents.models import Track, Content
from .models import Loving
from .serializers import LovingSerializer


class Lovings(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=LovingSerializer,
        responses={201: LovingSerializer},
    )
    def get(self, request):
        all_Lovings = Loving.objects.filter(user=request.user)
        serializer = LovingSerializer(
            all_Lovings,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=LovingSerializer,
        responses={201: LovingSerializer},
    )
    def post(self, request):
        serializer = LovingSerializer(data=request.data)
        if serializer.is_valid():
            loving = serializer.save(
                user=request.user,
            )
            tracks = request.data.get("track")
            for track_pk in tracks:
                track = Track.objects.get(pk=track_pk)
                loving.track.add(track)
            contents = request.data.get("content")
            for content_pk in contents:
                content = Content.objects.get(pk=content_pk)
                loving.content.add(content)
            serializer = LovingSerializer(loving)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class LovingDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Loving.objects.get(pk=pk, user=user)
        except Loving.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=LovingSerializer,
        responses={201: LovingSerializer},
    )
    def get(self, request, pk):
        loving = self.get_object(pk, request.user)
        serializer = LovingSerializer(
            loving,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=LovingSerializer,
        responses={201: LovingSerializer},
    )
    def delete(self, request, pk):
        loving = self.get_object(pk, request.user)
        loving.delete()
        return Response(status=HTTP_200_OK)

    @extend_schema(
        request=LovingSerializer,
        responses={201: LovingSerializer},
    )
    def put(self, request, pk):
        loving = self.get_object(pk, request.user)
        serializer = LovingSerializer(
            loving,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            loving = serializer.save()
            serializer = LovingSerializer(
                loving,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class LovingToggle(APIView):
    def get_list(self, pk, user):
        try:
            return Loving.objects.get(pk=pk, user=user)
        except Loving.DoesNotExist:
            raise NotFound

    def get_track(self, pk):
        try:
            return Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            raise NotFound

    def put(self, request, pk, room_pk):
        loving = self.get_list(pk, request.user)
        track = self.get_track(track_pk)
        if loving.tracks.filter(pk=track.pk).exists():
            loving.tracks.remove(track)
        else:
            loving.tracks.add(track)
        return Response(status=HTTP_200_OK)
