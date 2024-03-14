from django.shortcuts import render, HttpResponse
from scraper.scraper import Scraper
from ML_Utils.Sentiment import Sentiment



# Create your views here.
def news_analyzer(request):
    if "scrape_url" in request.POST:
        scraper = Scraper()
        sentiment = Sentiment()
        scrape_url = request.POST.get('scrape_url')
        if not scrape_url:
            return render(request=request, template_name="news_analyzer/analyzer.html")
        scraped_values = scraper.scrape(scrape_url)
        sentiment_result = sentiment.predict(scraped_values["Content"])
        context = {"news_title": scraped_values["Title"], "news_content": scraped_values["Content"], "sentiment":sentiment_result, "scrape_url":scrape_url}
        return render(request=request, template_name="news_analyzer/analyzer.html", context=context)

    return render(request=request, template_name="news_analyzer/analyzer.html")