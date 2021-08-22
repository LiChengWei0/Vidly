from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    # 界面中显示的顺序
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    # 界面中不显示的
    exclude = ('data_create', )
    list_display = ('title', 'number_in_stock', 'daily_rate')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)


