from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'new', 'author_name', 'author_email', 'content', 'is_approved', 'created_at']
        read_only_fields = ['id', 'is_approved', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['new'] = {
            'id': instance.new.id,
            'name': instance.new.title,
            'slug': instance.new.slug,
        }
        return representation