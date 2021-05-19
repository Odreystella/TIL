from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Level, Profile, Category, Article, Comment, Relationship, LikedArticle, LikedComment, Tag
from django.contrib import auth
# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }

    return render(request, 'index.html', context)

ERROR_MSG = {
    'FILLED_INPUT' : '필수항목을 채워주세요',
    'EXIST_ID' : '이미 존재하는 아이디 입니다.',
    'NO_EXIST_ID' : '존재하지 않는 아이디 입니다.',
    'PASSWORD_CHECK' : '비밀번호를 다시 입력해주세요',
    'PASSWORD_LENGTH' : '비밀번호는 8자리 이상이어야 합니다.',
}

def signup(request):
    context = {
        'error' : {
            'status' : False,
            'msg' : '',
        }
    }
    if request.method == 'POST':
        user_id = request.POST['userid']
        user_password = request.POST['userpassword']
        user_password_check = request.POST['userpasswordcheck']
        name = request.POST['name']

        if (not user_id or not user_password or not user_password_check):
            context['error']['status'] = True
            context['error']['msg'] = ERROR_MSG['FILLED_INPUT']
            return render(request, 'signup.html', context)

        user = User.objects.filter(username=user_id)
        if len(user) != 0:
            context['error']['status'] = True
            context['error']['msg'] = ERROR_MSG['EXIST_ID']
            return render(request, 'signup.html', context)

        if user_password != user_password_check:
            context['error']['status'] = True
            context['error']['msg'] = ERROR_MSG['PASSWORD_CHECK']
            return render(request, 'signup.html', context)

        if len(user_password) <= 8:
            context['error']['status'] = True
            context['error']['msg'] = ERROR_MSG['PASSWORD_LENGTH']
            return render(request, 'signup.html', context)


        if context['error']['status'] == False:
            user = User.objects.create_user(
                username=user_id,
                password=user_password
            )

            Profile.objects.create(
                user=user,
                name=name
            )

            Relationship.objects.create(
                user=user,
            )

            auth.login(request, user)
            return redirect('index')

    return render(request, 'signup.html', context)

def logout(request):
    auth.logout(request)
    return redirect('index')

def login(request):
    context = {
        'error' : {
            'status' : False,
            'msg' : '',
        }
    }
    if request.method == 'POST':
        user_id = request.POST['userid']
        user_password = request.POST['userpassword']

        if (not user_id or not user_password):
            context['error']['status'] = True
            context['error']['msg'] = ERROR_MSG['FILLED_INPUT']
            return render(request, 'login.html', context)

        try:
            user = User.objects.get(username=user_id)

        except:
            context['error']['status'] = True
            context['error']['msg'] = ERROR_MSG['NO_EXIST_ID']
            return render(request, 'login.html', context)

        auth_user = auth.authenticate(username=user_id, password=user_password)
        if auth_user:
            auth.login(request, user)
            return redirect('index')

    return render(request, 'login.html', context)

def category(request, category_pk):
    category = Category.objects.filter(pk=category_pk).first()
    articles = Article.objects.filter(category__pk=category_pk)
    new_articles = [article for article in articles if not article.is_deleted]
    context = {
        'category' : category,
        'articles' : new_articles,
    }
    return render(request, 'category.html', context)

def add(request, category_pk):
    category = Category.objects.filter(pk=category_pk).first()

    context={
        'category' : category,
        'error' : {
            'status' : False,
            'msg' : '',
        }
    }
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        if (not title or not content):
            context['error']['status'] = True
            context['error']['msg'] = ERROR_MSG['FILLED_INPUT']
            return render(request, 'article_add.html', context)
        
        if context['error']['status'] == False:
            Article.objects.create(
                category=category,
                author=request.user,
                title=title,
                content=content,
            )
            return redirect('category', category_pk)

    return render(request, 'article_add.html', context)

def detail(request, article_pk):
    article = Article.objects.filter(pk=article_pk).first()
    comments = Comment.objects.filter(article__pk=article_pk)

    #좋아요 여부를 알 수 있는 댓글들
    comments_list = []
    for comment in comments:
        is_liked = False
        if request.user in comment.liked_comment.users.all():
            is_liked = True
        data = {
            'is_liked' : is_liked,
            'comment' : comment,
            'count_of_likes' : len(comment.liked_comment.users.all()),
        }
        comments_list.append(data)
    
    #tag 목록
    tags = Tag.objects.filter(articles=article)

    context = {
        'article' : article,
        # 'comments' : comments,
        'comments' : comments_list,
        'tags' : tags,
    }
    return render(request, 'article_detail.html', context)

def edit(request, article_pk):
    article = Article.objects.filter(pk=article_pk).first()
    context = {
        'article' : article,
    }

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.filter(pk=article_pk).update(
            title=title,
            content=content,
        )
        return redirect('article-detail', article_pk)

    return render(request, 'article_edit.html', context)

def delete(request, article_pk):
    article = Article.objects.filter(pk=article_pk).first()
    category_pk = article.category.pk

    article.is_deleted = True
    Article.objects.filter(pk=article_pk).update(
        is_deleted=article.is_deleted
    )
    return redirect('category', category_pk )

def comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.filter(pk=article_pk).first()
   
    comment = request.POST['comment']
    if comment:
        comment = Comment.objects.create(
            article=article,
            commenter=request.user,
            content=comment
        )

        LikedComment.objects.create(
            comment=comment,
        )


    return redirect('article-detail', article_pk)

def view_profile_detail(request, commenter_pk):
    article_pk = Comment.objects.filter(commenter__pk=commenter_pk).first().article.pk
    commenter = User.objects.filter(pk=commenter_pk).first()
    comments = Comment.objects.filter(commenter__pk=commenter_pk)

    is_followed = False
    relationship = Relationship.objects.filter(user__pk=commenter_pk).first()
    if request.user in relationship.followers.all():
        is_followed = True
    
    context = {
        'article_pk' : article_pk,
        'commenter' : commenter,
        'comments' : comments,
        'is_followed' : is_followed,
    }
    return render(request, 'profile_detail.html', context)

def follow(request, following_pk):
    relationship = Relationship.objects.filter(user__pk=following_pk).first()

    if request.user in relationship.followers.all():
        relationship.followers.remove(request.user)
        return redirect('profile-detail', following_pk)

    relationship.followers.add(request.user)
    return redirect('profile-detail', following_pk) 

def liked(request, comment_pk):
    article_pk = Comment.objects.filter(pk=comment_pk).first().article.pk
    like = LikedComment.objects.filter(comment__pk=comment_pk).first()

    if request.user in like.users.all():
        like.users.remove(request.user)
        return redirect('article-detail', article_pk)

    like.users.add(request.user)  
    return redirect('article-detail', article_pk) 

def add_tag(request, article_pk):
    tag_name = request.POST['tag']
    tag = Tag.objects.filter(name=tag_name).first()
    article = Article.objects.filter(pk=article_pk).first()

    if tag:
        tag.articles.add(article)
        return redirect('article-detail', article_pk)

    new_tag = Tag.objects.create(name=tag_name)
    new_tag.articles.add(article)
    return redirect('article-detail', article_pk)

def view_tag_detail(request, tag_pk):
    tag = Tag.objects.filter(pk__in=[tag_pk]).first()
    # tag = Tag.objects.filter(pk=tag_pk).first()
    articles = tag.articles.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'tag_detail.html', context)