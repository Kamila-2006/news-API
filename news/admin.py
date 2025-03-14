from django.contrib import admin
from .models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'views_count', 'is_published', 'created_at', 'updated_at']
    search_fields = ('title', 'category',)
    exclude = ('slug',)