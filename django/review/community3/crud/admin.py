from django.contrib import admin
from .models import Level, Profile, Category, Article, Comment, Relationship, LikedArticle, LikedComment, Tag

# Register your models here.
admin.site.register(Level)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Relationship)
admin.site.register(LikedArticle)
admin.site.register(LikedComment)
admin.site.register(Tag)