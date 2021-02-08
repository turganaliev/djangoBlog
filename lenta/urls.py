from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_lenta),
    path('post-add/', views.add_post),
    path('posts/<int:pk>/', views.detail_post),
    path('post-edit/<int:pk>/', views.edit_post),
    path('like-add/', views.add_like),
    path('post-delete/<int:pk>/', views.delete_post),
]