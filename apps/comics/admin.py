from django.contrib import admin

from .models import Comic, Rating


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'rating',
        'author',
    )
    list_display_links = (
        'title',
    )
    search_fields = (
        'id',
        'title',
        'rating',
        'author',
    )
    list_filter = (
        'id',
        'title',
        'rating',
        'author',
    )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'comic_id',
        'user_id',
        'VALUE',
    )
    list_display_links = (
        'comic_id',
    )
    search_fields = (
        'id',
        'comic_id',
        'user_id',
        'VALUE',
    )
    list_filter = (
        'id',
        'comic_id',
        'user_id',
        'VALUE',
    )
