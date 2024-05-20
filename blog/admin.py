from django.contrib import admin
from .models import Blog, BlogAsset, BlogTag, BlogLike, Comment, CommentLike, Reply

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogAsset)
admin.site.register(BlogTag)
admin.site.register(BlogLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(Reply)
