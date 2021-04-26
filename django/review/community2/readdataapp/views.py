from django.shortcuts import render
from .models import Category, Article

# Create your views here.
def index(request):
    category_list = Category.objects.all()
    # print(category_list)
    context = {
        'category_list' : category_list,
    }
    return render(request, 'index.html', context)
