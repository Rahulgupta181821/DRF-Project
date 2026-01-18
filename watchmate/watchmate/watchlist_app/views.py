# from django.shortcuts import render

# # Create your views here.
# from watchlist_app.models import Move
# from django.http import JsonResponse
# def movie_list(request):
#     movies = Move.objects.all()
#     data = {
#         'movies':list(movies.values())
#     }
#     # print(movies.values())
#     return JsonResponse(data)

# def movie_detail(request, pk):
#     movie = Move.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active,
#     }
#     print("Movie:",movie)
#     return JsonResponse(data)
    
