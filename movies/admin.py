from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Genre, Movies
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'num_in_stock', 'daily_rate')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)