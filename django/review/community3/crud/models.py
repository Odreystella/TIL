from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.
class Level(models.Model):
    LEVEL_TYPES = [
        ('STANDARD', 'Standard'),
        ('SILVER', 'Silver'),
        ('GOLD', 'Gold'),
    ]
    rank = models.CharField(max_length=64, choices=LEVEL_TYPES)

    def __str__(self):
        return self.rank


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='profile')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True, related_name='profile')
    name = models.CharField(max_length=64)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='article')
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comment')
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.TextField(default=time.time())


class Relationship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='relationship')
    followers = models.ManyToManyField(User, blank=True, related_name='following')


class LikedArticle(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='liked_article')
    users = models.ManyToManyField(User, blank=True, related_name='liked_article') 


class LikedComment(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='liked_comment')
    users = models.ManyToManyField(User, blank=True, related_name='liked_comment') 


class Tag(models.Model):
    articles = models.ManyToManyField(Article, blank=True, related_name='tag')
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name



    




