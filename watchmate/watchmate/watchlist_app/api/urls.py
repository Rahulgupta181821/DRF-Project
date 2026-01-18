from django.urls import path, include
from watchlist_app.api.views import *
urlpatterns = [
    # path('list/',movie_list,name='movie-list'),
    # path('<int:pk>',movie_detail,name='movie-detail'),
    path('list/',MovieListAV.as_view(),name='movie-list'),
    path('<int:pk>',MovieDetailAV.as_view(),name='movie-detail'),
]
