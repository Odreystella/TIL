from django.contrib import admin
from .models import Category, Article, Profile, Comment, Relationship, LikeComment, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Relationship)
admin.site.register(LikeComment)
admin.site.register(Tag)