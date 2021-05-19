"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    #auth
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),

    #category
    path('category/<int:category_pk>', views.category, name='category'),

    #article
    path('article/add/<int:category_pk>', views.add, name='article-add'),
    path('article/detail/<int:article_pk>', views.detail, name='article-detail'),
    path('article/edit/<int:article_pk>', views.edit, name='article-edit'),
    path('article/delete<int:article_pk>', views.delete, name='article-delete'),

    #comment
    path('article/comment/<int:article_pk>', views.comment, name='comment'),
    path('profile-detail/<int:commenter_pk>', views.view_profile_detail, name='profile-detail'),

    #follow
    path('follow/<int:following_pk>', views.follow, name='follow'),

    #like
    path('like/<int:comment_pk>',views.liked, name='like'),

    #tag
    path('tag/<int:article_pk>',views.add_tag, name='tag'),
    path('tag/detail/<int:tag_pk>', views.view_tag_detail, name='tag-detail'),
]
