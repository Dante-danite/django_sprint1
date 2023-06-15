from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index),
    path('posts/<int:id>/', views.post_detail,),
    path('category/<slug:category>/', views.category_posts)
]
