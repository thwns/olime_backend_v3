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

    def get(self, request):
        all_followings = Following.objects.filter(user=request.user)
        serializer = FollowingSerializer(
            all_followings,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = FollowingSerializer(data=request.data)
        if serializer.is_valid():
            following = serializer.save(
                user=request.user,
            )
            tracks = request.data.get("tracks")
            for track_pk in tracks:
                track = Track.objects.get(pk=track_pk)
                following.tracks.add(track)
            serializer = FollowingSerializer(following)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FollowingDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Following.objects.get(pk=pk, user=user)
        except Following.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        following = self.get_object(pk, request.user)
        serializer = FollowingSerializer(
            following,
            context={"request": request},
        )
        return Response(serializer.data)

    def delete(self, request, pk):
        following = self.get_object(pk, request.user)
        following.delete()
        return Response(status=HTTP_200_OK)

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

    def put(self, request, pk, room_pk):
        following = self.get_list(pk, request.user)
        track = self.get_track(track_pk)
        if following.tracks.filter(pk=track.pk).exists():
            following.tracks.remove(track)
        else:
            following.tracks.add(track)
        return Response(status=HTTP_200_OK)
