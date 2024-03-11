from django.urls import path, include
from news_analyzer import views


urlpatterns = [
    path('', views.news_analyzer, name='news_analyzer'),
]
