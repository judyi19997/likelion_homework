"""likelion8th URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import wordcount.views
import Blog.views
import account.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wordcount/', wordcount.views.wordcount, name = "wordcount"),
    path('result/',wordcount.views.result, name = "result"),
    path('', Blog.views.begin, name="begin"),
    path('blog/<int:blog_id>',Blog.views.detail, name = "detail"),
    path('blog/new',Blog.views.new, name = "new"),
    path('blog/create',Blog.views.create, name = "create"),
    path('blog/update/<int:select_id>',Blog.views.update, name = "update"),
    path('blog/edit/<int:select_id>',Blog.views.edit, name = "edit"),
    path('blog/delete/<int:select_id>',Blog.views.delete, name = 'delete'),
    path('account/', include(account.urls)),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #media url