from rest_framework import serializers
from .models import New


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'slug', 'content', 'category', 'tags', 'image', 'views_count', 'is_published', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'views_count', 'is_published', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = {
            'id': instance.category.id,
            'name': instance.category.name,
            'slug': instance.category.slug,
        }
        representation['tags'] = [
            {
                'id': tag.id,
                'name': tag.name,
                'slug': tag.slug
            }
            for tag in instance.tags.all()
        ]
        return representation