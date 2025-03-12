from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['id', 'new', 'author_name', 'author_email', 'is_approved', 'created_at']
    search_fields = ('new', 'author_name', 'author_email')
    exclude = ('slug', )