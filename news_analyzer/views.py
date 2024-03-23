from django.shortcuts import render, HttpResponse
from scraper.scraper import Scraper
from ML_Utils.Sentiment import Sentiment
from ML_Utils.TextAnalyzer import TextAnalyzer
from Stemmer import Stemmer
from django.views import View
from .forms import NewsAnalyzerForm



# Create your views here.
class NewsAnalyzerView(View):
    def post(self, request):
        # Checks if there were any problems during scraping
        scraping_issue = False
        if "scrape_url" in request.POST:
            scraper = Scraper()
            scrape_url = request.POST.get('scrape_url')
            model_choice = request.POST.get('model_choice')
            sentiment = Sentiment(model=model_choice)
            text_analyzer = TextAnalyzer()
            stemmer = Stemmer()
            if not scrape_url:
                return render(request=request, template_name="news_analyzer/analyzer.html")
            try:
                scraped_values = scraper.scrape(scrape_url)
                input_text = stemmer.stem(scraped_values["Content"])
                sentiment_result = sentiment.predict(input_text)
                probabilities = sentiment.get_probabilities(input_text)
                most_common_words = text_analyzer.get_most_frequent_words(input_text, 6)
                context = {"news_title": scraped_values["Title"], 
                           "news_content": scraped_values["Content"], 
                           "sentiment": sentiment_result, 
                           "scrape_url": scrape_url,
                           "scraping_issue": scraping_issue, 
                           "probabilities": probabilities,
                           "model_choice": model_choice,
                           "common_words": most_common_words}
                return render(request=request, template_name="news_analyzer/analyzer.html", context=context)
            except:
                scraping_issue = True
                return render(request=request, template_name="news_analyzer/analyzer.html", context={"model_choice":model_choice, "scrape_url": scrape_url, "scraping_issue": scraping_issue})

    def get(self, request):
        # Handle GET requests (if needed)
        return render(request=request, template_name="news_analyzer/analyzer.html")

