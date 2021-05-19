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
from readdataapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('category/<int:category_pk>', views.category, name='category'),
    path('detail/<int:article_pk>', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:article_pk>', views.edit, name='edit'),
    path('delete/<int:article_pk>', views.delete, name='delete'),

    # auth
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile_detail/<int:writer_pk>', views.profile_detail, name='profile_detail'),

    #comment
    path('comment/<int:article_pk>', views.comment, name='comment'),
    
    #follow
    path('follow/<int:writer_pk>', views.follow, name='follow'),
]
