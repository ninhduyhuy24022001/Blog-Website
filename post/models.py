from django.db import models
from django.utils.text import slugify

from core.models import User

class Category(models.Model):
    # parend_id
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name_plural = "categories"

class Tag(models.Model):
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # parent_id 
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=255)
    published =models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to="post_image", blank=True, null=True)

    categories = models.ManyToManyField(Category, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
    
class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='metas')
    key = models.CharField(max_length=50, unique=True)
    content = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f"{self.post.title}"

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # parent_id
    title = models.CharField(max_length=100)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.title}"