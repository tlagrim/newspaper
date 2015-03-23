# Homepage views
from django.shortcuts import render
from featured.models import MainStory, FeaturedArticle
from articles.models import Article
from sections.models import Section


def homepage(request):
    main_article_ids = [mainStory['article_id'] for mainStory in MainStory.objects.values()]
    main_articles = [Article.objects.get(pk=i) for i in main_article_ids]

    featured_article_ids = [(featured_article['article_id'], featured_article['section_id'])
                            for featured_article in FeaturedArticle.objects.values()]
    featured_articles = [(Article.objects.get(pk=a_id), Section.objects.get(pk=s_id))
                         for (a_id, s_id) in featured_article_ids]

    template_context = {}
    template_context['main_stories'] = main_articles
    template_context['featured_articles'] = featured_articles

    return render(request, 'homepage.html', template_context)
