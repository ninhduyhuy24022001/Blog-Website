from django.contrib import admin

from .models import Post, PostMeta, PostComment, Category, Tag

admin.site.register(Post)
admin.site.register(PostMeta)
admin.site.register(PostComment)
admin.site.register(Category)
admin.site.register(Tag)