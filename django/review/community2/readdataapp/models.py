from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article')
    writer = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    contents = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_delated = models.BooleanField(default=False)

    def __str__(self):
        return self.title