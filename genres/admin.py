from django.contrib import admin
from .models import Genre


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    list_display = ('id', 'name')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
