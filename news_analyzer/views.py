from django.shortcuts import render, HttpResponse
from scraper.scraper import Scraper
from ML_Utils.Sentiment import Sentiment



# Create your views here.
def news_analyzer(request):
    # Checks if there were any problems during scraping
    scraping_issue = False
    if request.method == 'POST':
        if "scrape_url" in request.POST:
            scraper = Scraper()
            scrape_url = request.POST.get('scrape_url')
            model_choice = request.POST.get('model_choice')
            sentiment = Sentiment(model=model_choice)
            if not scrape_url:
                return render(request=request, template_name="news_analyzer/analyzer.html")
            try:
                scraped_values = scraper.scrape(scrape_url)
                sentiment_result = sentiment.predict(scraped_values["Content"])
                context = {"news_title": scraped_values["Title"], 
                        "news_content": scraped_values["Content"], 
                        "sentiment":sentiment_result, 
                        "scrape_url":scrape_url, "scraping_issue":scraping_issue}
                return render(request=request, template_name="news_analyzer/analyzer.html", context=context)
            except:
                scraping_issue = True
                return render(request=request, template_name="news_analyzer/analyzer.html", context={"scrape_url":scrape_url, "scraping_issue":scraping_issue})
    return render(request=request, template_name="news_analyzer/analyzer.html")