from django.urls import path

from .views import ComicRatingView, RatingCreateView


urlpatterns = [
    path('rating/', RatingCreateView.as_view(), name='create-rating'),
    path('comics/<int:pk>/rating/', ComicRatingView.as_view(), name='get-comic-rating'),
]
