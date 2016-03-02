# Contributor Views
from django.shortcuts import render
from contributors.models import Contributor
from articles.models import Article


# Create your views here.
def contributor_page(request, contributor_url):
    contributor = Contributor.objects.get(twitter=contributor_url)
    return render(request, 'contributor.html', {'contributor': contributor})