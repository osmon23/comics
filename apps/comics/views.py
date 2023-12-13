from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Comic, Rating
from .serializers import ComicSerializer, RatingSerializer


class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comic_id = serializer.validated_data['comic_id'].id
        user_id = serializer.validated_data['user_id'].id

        existing_rating = Rating.objects.filter(comic_id=comic_id, user_id=user_id).first()

        if existing_rating:
            existing_rating.VALUE = serializer.validated_data['VALUE']
            existing_rating.save()
        else:
            serializer.save()

        ratings = Rating.objects.filter(comic_id=comic_id)
        total_ratings = ratings.count()
        if total_ratings > 0:
            average_rating = sum(r.VALUE for r in ratings) / total_ratings
            comic = Comic.objects.get(id=comic_id)
            comic.rating = round(average_rating, 2)
            comic.save()


class ComicRatingView(generics.RetrieveAPIView):
    serializer_class = ComicSerializer
    queryset = Comic.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
