from django.shortcuts import render
from django.views.generic import View
from main.models import Movie

class HomeView(View):
    def get(self, request):
        query = request.GET.get("search")

        if query:
            allMovies = Movie.objects.filter(name__icontains=query)
        else:
            allMovies = Movie.objects.all()

        context = {
            "movies": allMovies,
        }

        return render(request, 'main/index.html', context)


class DetailView(View):
    def get(self, request, id):
        movie = Movie.objects.get(id=id)

        context = {
            "movie": movie,
        }

        return render(request, 'main/detail.html', context)
