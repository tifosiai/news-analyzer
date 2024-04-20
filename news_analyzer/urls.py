from django.urls import path, include
from news_analyzer import views


urlpatterns = [
    path('', views.NewsAnalyzerView.as_view(), name="news_analyzer"),
    path('scraper', views.AutoNewsAnalyzerView.as_view(), name='auto_news_analyzer'),
    path('manual', views.ManualNewsAnalyzerView.as_view(), name='manual_news_analyzer'),
]
