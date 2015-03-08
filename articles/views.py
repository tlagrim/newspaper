#articles views
from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article

# Create your views here.

def article_page(request, article_url):
	article = Article.objects.get(url=article_url)
	return render(request, 'article.html', {'article': article})	