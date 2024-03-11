from django.shortcuts import render
# from ML_Utils.Sentiment import Sentiment
# from ML_Utils.stemming import stem_sentence
# from ML_Utils.utils import load_pos_model
# # Create your views here.

# sentiment = Sentiment()

def home_page(request):
#     text = """Yaşayış binaları ilə bağlı bəzi pilot layihələri həyata keçirən şirkətlərdən narazılıqlar var. Bəzən bu şirkətlər tikdikləri binaları vətəndaşlara söz verdikləri vaxtda təhvil verə bilmirlər.  

# Bakıda bir çox istifadəyə yararsız, köhnə tikililər sökülür, onların yerində yeni çoxmərtəbəli binalar inşa edilir. Bu işlər pilot layihələr çərçivəsində aparılır. Adətən tikinti şirkətləri sökülən tikililərdə yaşayan sakinlərlə müqavilə imzalayırlar və onları yeni bina tikilənə qədər kirayə pulu ilə təmin edirlər. Lakin bəzi hallarda tikinti şirkətləri binanı söz verdikləri vaxtda təhvil verə bilmirlər. Bu zaman tikinti şirkətləri və vətəndaşlar arasında narazılıqlar yaranır. Bəs görəsən binaların vaxtında təhvil verilməməsinin səbəbi nədir? Bu halla üzləşən vətəndaş hüquqlarını necə qoruya bilər?"""
#     model, w2i, idx2tag = load_pos_model()
#     res = stem_sentence(text, model, w2i, idx2tag)
    return render(request, "home/homepage.html",)


def about_page(request):
    return render(request, template_name="home/aboutpage.html")