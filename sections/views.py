# section views
from django.http import HttpResponse
from django.shortcuts import render
from sections.models import Section, Category
from articles.models import Article

# Create your views here.
def section_page(request, section_url):
  section = Section.objects.get(url=section_url)
  return render(request, 'section.html', {'section': section})


def category_page(request, category_url):
  category = Category.objects.get(url=category_url)
  response = str(category) + "\n"
  return HttpResponse(response)