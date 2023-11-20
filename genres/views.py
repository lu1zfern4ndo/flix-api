from django.http import JsonResponse
from .models import Genre


def genre_list(request):
    genres = Genre.objects.all()
    data = [{'id': genre.id, 'name': genre.name} for genre in genres]
    return JsonResponse({'genres': data})