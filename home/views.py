from django.shortcuts import render
from ML_Utils.Sentiment import Sentiment
from Stemmer import Stemmer


stemmer = Stemmer()
sentiment = Sentiment()


def home_page(request):
    text = "Salam mənim adım Ramildir."
    res = stemmer.stem(text)
    print(res)
    return render(request, "home/homepage.html")


def about_page(request):
    return render(request, template_name="home/aboutpage.html")