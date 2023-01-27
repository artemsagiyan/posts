from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['pk']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['pk']

