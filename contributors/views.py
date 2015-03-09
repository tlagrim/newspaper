# Contributor Views
from django.http import HttpResponse
from contributors.models import Contributor
from articles.models import Article

# Create your views here.
def contributor_page(request, contributor_url):
  contributor = Contributor.objects.get(twitter=contributor_url)
  articles = Article.objects.filter(author=contributor)

  response = str(contributor) + "\n"
  for article in articles:
    response += str(article) + "\n"

  return HttpResponse(response)