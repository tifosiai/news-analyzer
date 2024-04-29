from django.shortcuts import render, HttpResponse
from scraper.scraper import Scraper
from ML_Utils.Sentiment import Sentiment
from ML_Utils.TextAnalyzer import TextAnalyzer
from ML_Utils.CategoryClassifier import CategoryClassifier
from Stemmer import Stemmer
from django.views import View
from django.views.generic import TemplateView
from .forms import NewsAnalyzerForm



class NewsAnalyzerView(TemplateView):
    template_name="news_analyzer/news_analyzer.html"


class AutoNewsAnalyzerView(View):
    def post(self, request):
        # Checks if there were any problems during scraping
        scraping_issue = False
        if "scrape_url" in request.POST:
            scraper = Scraper()
            scrape_url = request.POST.get('scrape_url')
            model_choice = request.POST.get('model_choice')
            sentiment = Sentiment(model=model_choice)
            category_classifier = CategoryClassifier()
            text_analyzer = TextAnalyzer()
            stemmer = Stemmer()
            if not scrape_url:
                return render(request=request, template_name="news_analyzer/auto_analyzer.html")
            try:
                scraped_values = scraper.scrape(scrape_url)
                input_text = stemmer.stem(scraped_values["Content"])
                positive_counter, normalized_positive_counter, negative_counter, normalized_negative_counter = text_analyzer.get_lexicon_distribution(input_text)
                normalized_distribution = [normalized_positive_counter, normalized_negative_counter]
                sentiment_result = sentiment.predict(input_text)
                sentiment_probabilities = sentiment.get_probabilities(input_text)
                category_result = category_classifier.predict_category(input_text).capitalize()
                category_label_probabilities = category_classifier.get_category_probabilities(input_text)
                category_labels = list(category_label_probabilities.keys())
                category_probabilities = list(category_label_probabilities.values())
                most_common_words = text_analyzer.get_most_frequent_words(input_text, 6)
                context = {"news_title": scraped_values["Title"], 
                           "news_content": scraped_values["Content"], 
                           "sentiment": sentiment_result, 
                           "category": category_result,
                           "scrape_url": scrape_url,
                           "scraping_issue": scraping_issue, 
                           "sentiment_probabilities": sentiment_probabilities,
                           "category_probabilities": category_probabilities,
                           "category_max_probability": max(category_probabilities),
                           "category_labels": category_labels,
                           "positive_counter": positive_counter,
                           "normalized_distribution": normalized_distribution,
                           "negative_counter": negative_counter,
                           "model_choice": model_choice,
                           "common_words": most_common_words}
                return render(request=request, template_name="news_analyzer/auto_analyzer.html", context=context)
            except:
                scraping_issue = True
                return render(request=request, template_name="news_analyzer/auto_analyzer.html", context={"model_choice":model_choice, "scrape_url": scrape_url, "scraping_issue": scraping_issue})

    def get(self, request):
        # Handle GET requests (if needed)
        return render(request=request, template_name="news_analyzer/auto_analyzer.html")



class ManualNewsAnalyzerView(View):
    def post(self, request):
        # Checks if there were any problems during scraping
        scraping_issue = False
        if "content" in request.POST:
            content = request.POST.get('content')
            model_choice = request.POST.get('model_choice')
            sentiment = Sentiment(model=model_choice)
            text_analyzer = TextAnalyzer()
            stemmer = Stemmer()
            category_classifier = CategoryClassifier()
            if not content:
                return render(request=request, template_name="news_analyzer/manual_analyzer.html")
            try:
                input_text = stemmer.stem(content)
                sentiment_result = sentiment.predict(input_text)
                positive_counter, normalized_positive_counter, negative_counter, normalized_negative_counter = text_analyzer.get_lexicon_distribution(input_text)
                normalized_distribution = [normalized_positive_counter, normalized_negative_counter]
                sentiment_probabilities = sentiment.get_probabilities(input_text)
                category_result = category_classifier.predict_category(input_text).capitalize()
                category_label_probabilities = category_classifier.get_category_probabilities(input_text)
                category_labels = list(category_label_probabilities.keys())
                category_probabilities = list(category_label_probabilities.values())
                most_common_words = text_analyzer.get_most_frequent_words(input_text, 6)
                context = { "sentiment": sentiment_result, 
                           "category": category_result,
                           "content": content,
                           "scraping_issue": scraping_issue, 
                           "sentiment_probabilities": sentiment_probabilities,
                           "category_probabilities": category_probabilities,
                           "category_max_probability": max(category_probabilities),
                           "category_labels": category_labels,
                           "positive_counter": positive_counter,
                           "normalized_distribution": normalized_distribution,
                           "negative_counter": negative_counter,
                           "model_choice": model_choice,
                           "common_words": most_common_words}
                return render(request=request, template_name="news_analyzer/manual_analyzer.html", context=context)
            except:
                scraping_issue = True
                return render(request=request, template_name="news_analyzer/manual_analyzer.html", context={"model_choice":model_choice, "content": content})

    def get(self, request):
        # Handle GET requests (if needed)
        return render(request=request, template_name="news_analyzer/manual_analyzer.html")