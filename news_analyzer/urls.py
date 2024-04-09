from django.urls import path, include
from news_analyzer import views


urlpatterns = [
    path('scraper', views.NewsAnalyzerView.as_view(), name='news_analyzer'),
    path('manual', views.ManualNewsAnalyzerView.as_view(), name='manual_analyzer'),
]
