import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Genre


@csrf_exempt
def genre_create_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse({'genres': data})
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data.get('name'))
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201)
