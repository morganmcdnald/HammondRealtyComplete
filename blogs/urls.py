from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs'),
    path('<int:blog_id>', views.blog, name='blog'),
    path('blogSearch', views.search, name='blogSearch'),
]