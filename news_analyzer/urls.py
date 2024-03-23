from django.urls import path, include
from news_analyzer import views


urlpatterns = [
    path('', views.NewsAnalyzerView.as_view(), name='news_analyzer'),
]
