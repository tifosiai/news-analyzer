from django.shortcuts import render


def home_page(request):
    return render(request, "home/homepage.html")


def about_page(request):
    return render(request, template_name="home/aboutpage.html")


def contact(request):
    return render(request=request, template_name="home/contact.html")