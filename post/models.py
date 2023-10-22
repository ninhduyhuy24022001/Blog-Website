from django.db import models

from core.models import User



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # parent_id 
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField(255)
    published =models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField(2000, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='metas')
    key = models.CharField(max_length=50, unique=True)
    content = models.TextField(max_length=2000, blank=True, null=True)

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # parent_id
    title = models.CharField(max_length=100)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField(max_length=1000)

class Category(models.Model):
    # parend_id
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(max_length=255, blank=True, null=True)

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')

class Tag(models.Model):
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(max_length=255, blank=True, null=True)

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post')
    
