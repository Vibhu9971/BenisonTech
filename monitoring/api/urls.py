from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('log/', views.Logs.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]
