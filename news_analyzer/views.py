from django.shortcuts import render

# Create your views here.
def news_analyzer(request):
    return render(request=request, template_name="news_analyzer/analyzer.html")