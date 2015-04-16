# section views
from django.http import HttpResponse
from django.shortcuts import render

from sections.models import Section, Category
from articles.models import Article
from featured.models import FeaturedArticle


# Create your views here.
def section_page(request, section_url):
    section = Section.objects.get(url=section_url)
    featured_article = FeaturedArticle.objects.get(section=section).article
    articles = Article.objects.filter(section=section).exclude(url=featured_article.url)

    template_context = {}
    template_context['section'] = section
    template_context['featured_article'] = featured_article
    template_context['articles'] = articles

    return render(request, 'section.html', template_context)


def category_page(request, category_url):
    category = Category.objects.get(url=category_url)
    response = str(category) + "\n"
    return HttpResponse(response)