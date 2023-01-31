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
from contents.models import Track
from .models import Following
from .serializers import FollowingSerializer


class Followings(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=FollowingSerializer,
        responses={201: FollowingSerializer},
    )
    def get(self, request):
        all_followings = Following.objects.filter(user=request.user)
        serializer = FollowingSerializer(
            all_followings,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=FollowingSerializer,
        responses={201: FollowingSerializer},
    )
    def post(self, request):
        serializer = FollowingSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    following = serializer.save(
                        user=request.user,
                    )
                    tracks = request.data.get("tracks")
                    for track_pk in tracks:
                        try:
                            track = Track.objects.get(pk=track_pk)
                        except Track.DoesNotExist:
                            following.delete()
                            raise ParseError(
                                f"Track with id {track_pk} not found")
                        following.tracks.add(track)
                    serializer = FollowingSerializer(following)
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Track not found")
        else:
            return Response(serializer.errors)


class FollowingDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Following.objects.get(pk=pk, user=user)
        except Following.DoesNotExist:
            raise NotFound

    @extend_schema(
        request=FollowingSerializer,
        responses={201: FollowingSerializer},
    )
    def get(self, request, pk):
        following = self.get_object(pk, request.user)
        serializer = FollowingSerializer(
            following,
            context={"request": request},
        )
        return Response(serializer.data)

    @extend_schema(
        request=FollowingSerializer,
        responses={201: FollowingSerializer},
    )
    def delete(self, request, pk):
        following = self.get_object(pk, request.user)
        following.delete()
        return Response(status=HTTP_200_OK)

    @extend_schema(
        request=FollowingSerializer,
        responses={201: FollowingSerializer},
    )
    def put(self, request, pk):
        following = self.get_object(pk, request.user)
        serializer = FollowingSerializer(
            following,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            following = serializer.save()
            serializer = FollowingSerializer(
                following,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FollowingToggle(APIView):
    def get_list(self, pk, user):
        try:
            return Following.objects.get(pk=pk, user=user)
        except Following.DoesNotExist:
            raise NotFound

    def get_track(self, pk):
        try:
            return Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            raise NotFound

    def put(self, request, pk, track_pk):
        following = self.get_list(pk, request.user)
        track_list = self.get_track(track_pk)
        if following.track.filter(pk=track.pk).exists():
            following.track.remove(track_list)
        else:
            following.track.add(track_list)
        return Response(status=HTTP_200_OK)
