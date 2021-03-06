from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True, blank=True)
    title = models.CharField(max_length=64)
    contents = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_delated = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='profile', null=True, blank=True)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    residence = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.TextField(default=time.time())

    def __str__(self):
        return self.name 


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name='comments', null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True, blank=True )
    contents = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.TextField(default=time.time())


class Relationship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='relationship')
    followers =  models.ManyToManyField(User, related_name='following',blank=True)


class LikeComment(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='like_comment')
    user = models.ManyToManyField(User, blank=True, related_name='like_comment')
    

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    articles = models.ManyToManyField(Article, blank=True, related_name='tag')
