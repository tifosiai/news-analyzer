from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact, name='contact'),
]
