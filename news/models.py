from django.db import models
from categories.models import Category
from tags.models import Tag


class New(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    tags = models.ManyToManyField(Tag, related_name='news')
    image = models.ImageField(required=False)
    views_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)