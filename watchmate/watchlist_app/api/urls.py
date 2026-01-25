from django.urls import path, include
from watchlist_app.api.views import *
urlpatterns = [
    # path('list/',movie_list,name='movie-list'),
    # path('<int:pk>',movie_detail,name='movie-detail'),
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlateformAV.as_view(),name='stream-list'),
    path('stream/<int:pk>',StreamPlateformDetailAV.as_view(),name='stream-detail'),
    
    path('review/',ReviewList.as_view(),name="review-list"),
    path('review/<int:pk>',ReviewDetail.as_view(),name="review-detail")
    
]
