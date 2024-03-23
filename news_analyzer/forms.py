from django import forms
    
class NewsAnalyzerForm(forms.Form):
    scrape_url = forms.URLField(label="Scrape Url", required=True)
    model_choice = forms.ChoiceField(label="Model Choice", choices=[
        ('', 'Select a Model'),
        ('nn', 'Neural Network (95.3%)'),
        ('svm', "Support Vector Classifier (95.0%)"),
        ('nb', 'Naive Bayes (92.3%)'),
        ('lr', 'Logistic Regression (92.1%)'),
        ('knn', 'K-Nearest Neigbors (91.7%)'),
    ],)