from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Article
from django.urls import path
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    categories = Category.objects.all()
    # category_len = len(category_list)
    new_article_pk = Article.objects.all().last().pk + 1
    print(new_article_pk)
    context = {
        'categories' : categories,
        'category_len' : len(categories),
        'category_pk' : 7,
        # 'new_article_pk' : new_article_pk,
    }
    return render(request, 'index.html', context)

def category(request, category_pk):
    category = Category.objects.filter(pk=category_pk).first()
    # categort = get_object_or_404(Category, pk=category_pk)
    context = {
        'category' : category,
        'category_pk': category_pk,
    }
    # print(category.article.all())
    return render(request, 'category.html', context)

def detail(request, article_pk):
    article = Article.objects.filter(pk=article_pk).first()
    # article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article,
        'article_pk' : article_pk,
    }
    return render(request, 'detail.html', context)

def add(request, category_pk):
    categories = Category.objects.all()
    article = Article.objects.all()
    category = get_object_or_404(Category, pk=category_pk)
    context = {
        'categories' : categories,
        'article' : article,
        'category_pk' : category.pk,
        # 'category_pk_home' : request.POST['category_pk_home'],
        # 'pk' : target_category,
        # 'new_article_pk' : new_article_pk,
        'error' : {
            'state' : False,
            'msg' : '',
        }
    } 
                
    if request.method == 'POST':
        pk_category = request.POST['pk_category']
        title = request.POST['title']
        writer = request.POST['writer']
        contents = request.POST['contents']   
        print(category_pk)

        if (title and contents and writer):

            target_category = get_object_or_404(Category, pk=pk_category)   

            article = Article.objects.create(
                category=target_category,
                title=title,
                writer=writer,
                contents=contents,
            )
            return redirect('category', category_pk)

        else:
            context['error']['state'] = True
            context['error']['msg'] = '작성하지 않은 항목을 채워주세요.'
    
    return render(request, 'add.html', context)

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article,            
        'article_pk' : article_pk,
    }

    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents'] 
        print(contents)

        Article.objects.filter(pk=article_pk).update(
            title=title,
            contents=contents
        )         
        return redirect('detail', article_pk)

    return render(request, 'edit.html', context)

def delete(request, article_pk):
    # 실제로 데이터 삭제하는 방법
    # target_article = get_object_or_404(Article, pk=article_pk)
    # target_article_pk = target_article.pk
    # category_pk = target_article.category.pk
    # target_article.delete()

    target_article = get_object_or_404(Article, pk=article_pk)
    category_pk = target_article.category.pk
    target_article.is_delated = True
    Article.objects.filter(pk=article_pk).update(
        is_delated=target_article.is_delated
    )
    print(target_article.is_delated)

    return redirect('category', category_pk)

def signup(request):
    error_msg = {
            'FILLED_INPUT' : '필수항목을 채워주세요',
            'EXIST_ID' : '이미 존재하는 아이디입니다.',
            'PASSWORD_CHECK' : '비밀번호를 다시 입력해주세요', 
    }
    context = {
        'error' : {
            'state' : False,
            'msg' : error_msg,
        }
    }
   
    if request.method =='POST':
        userid = request.POST['userid']
        password = request.POST['password']
        password_check = request.POST['password_check']
        user = User.objects.filter(username=userid)
        
        if (not userid or not password or not password_check):
            context['error']['state'] = True
            context['error']['msg'] = error_msg['FILLED_INPUT']
            
        if len(user) != 0: # 유저 아이디가 존재하니?
            context['error']['state'] = True
            context['error']['msg'] = error_msg['EXIST_ID']

        if password != password_check:
            context['error']['state'] = True
            context['error']['msg'] = error_msg['PASSWORD_CHECK']

        if context['error']['state'] == False:
            # 아래는 state == False일 때 실행되어야 함    
            user = User.objects.create_user(
                    username=userid,
                    password=password,
            )

            auth.login(request, user)

            return redirect('index')      

    return render(request, 'signup.html', context)

# before refactorting
"""
def signup(request):
    error_msg = {
            'FILLED_INPUT' : '필수항목을 채워주세요',
            'EXIST_ID' : '이미 존재하는 아이디입니다.',
            'PASSWORD_CHECK' : '비밀번호를 다시 입력해주세요', 
    }
    context = {
        'error' : {
            'state' : False,
            'msg' : error_msg,
        }
    }
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']
        password_check = request.POST['password_check']
        user = User.objects.filter(username=userid)

        if (userid and password and password_check):

            if len(user) == 0: 
            
                if password == password_check:
                    user = User.objects.create_user(
                        username=userid,
                        password=password,
                    )
                    auth.login(request, user)
                    return redirect('index')

                else :
                    context['error']['state'] = True
                    context['error']['msg'] = error_msg['PASSWORD_CHECK']

            else:
                context['error']['state'] = True
                context['error']['msg'] = error_msg['EXIST_ID']

        else:
            context['error']['state'] = True
            context['error']['msg'] = error_msg['FILLED_INPUT']

    return render(request, 'signup.html', context)
"""

