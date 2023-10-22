from django.contrib import admin

from .models import Post, PostMeta, PostComment, Category, PostCategory, Tag, PostTag

admin.site.register(Post)
admin.site.register(PostMeta)
admin.site.register(PostComment)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Tag)
admin.site.register(PostTag)
