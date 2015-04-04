# Homepage views
from django.shortcuts import render
from featured.models import MainStory, FeaturedArticle, PinnedArticle
from articles.models import Article
from sections.models import Section


def homepage(request):
    # main articles
    main_article_ids = [mainStory['article_id'] for mainStory in MainStory.objects.values()]
    main_articles = [Article.objects.get(pk=i) for i in main_article_ids]

    # featured articles
    featured_article_ids = [(featured_article['article_id'], featured_article['section_id'])
                            for featured_article in FeaturedArticle.objects.values()]
    featured_articles = [(Article.objects.get(pk=a_id), Section.objects.get(pk=s_id))
                         for (a_id, s_id) in featured_article_ids]

    # pinned articles
    pinned_article_ids = [pinned_article['article_id'] for pinned_article in PinnedArticle.objects.values()]
    # split pinned articles into rows
    pinned_articles = list(chunk([Article.objects.get(pk=i) for i in pinned_article_ids], 3))

    # build context
    template_context = {}
    template_context['main_stories'] = main_articles
    template_context['featured_articles'] = featured_articles
    template_context['pinned_articles'] = pinned_articles

    return render(request, 'homepage.html', template_context)

def chunk(articles, row_size):
    for i in range(0, len(articles), row_size):
        yield articles[i:i+row_size]