from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<int:pk>/', views.post, name="post"),
    path('create/', views.create, name="create-post"),
    path('delete/', views.delete_all, name="delete_all"),
]