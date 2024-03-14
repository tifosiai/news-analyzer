from django.shortcuts import render
from ML_Utils.Sentiment import Sentiment
from Stemmer import Stemmer


def home_page(request):
    return render(request, "home/homepage.html")


def about_page(request):
    return render(request, template_name="home/aboutpage.html")