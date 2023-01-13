from django.contrib import admin
from .models import Track, Content, Book, Lecture


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'followers_num', 'created_at', 'updated_at',
    )
    list_filter = (
        'followers_num', 'category',
    )
    search_fields = (
        'name',
        'leader__username',
    )
    readonly_field = (
        'created_at', 'updated_at',
    )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):

    list_display = (
        'name',  'total_tracks', 'types', 'created_at', 'updated_at',
    )
    list_filter = (
        'types', 'category',
    )
    search_fields = (
        'name',
    )
    readonly_field = (
        'created_at', 'updated_at',
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        'title', 'author', 'created_at', 'updated_at',
    )
    list_filter = (
        'company',
    )
    search_fields = (
        'title',
    )
    readonly_field = (
        'created_at', 'updated_at',
    )


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'created_at', 'updated_at',
    )
    list_filter = (
        'company',
    )
    search_fields = (
        'title',
    )
    readonly_field = (
        'created_at', 'updated_at',
    )
