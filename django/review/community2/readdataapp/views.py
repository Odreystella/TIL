from django.shortcuts import render
from .models import Category, Article

# Create your views here.
def index(request):
    category_list = Category.objects.all()
    # category_len = len(category_list)
    context = {
        'category_list' : category_list,
        'category_len' : len(category_list)
    }
    return render(request, 'index.html', context)

def category(request, category_pk):
    category = Category.objects.filter(pk=category_pk).first()
    context = {
        'category' : category,
    }
    # print(category.article.all())
    return render(request, 'category.html', context)

def detail(request, article_pk):
    article = Article.objects.filter(pk=article_pk).first()
    context = {
        'article' : article,
    }
    return render(request, 'detail.html', context)