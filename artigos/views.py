from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse

from artigos.models import Article


# Create your views here.
def home(request, template_name="artigos/pages/home.html"):
    articles = Article.objects.filter(is_published=True).order_by('-id')
    current_page = request.GET.get('page', 1)
    paginator = Paginator(articles, 8)
    page_obj = paginator.get_page(current_page)
    args = {}
    name = "Cesar Luiz Ferracin"
    args['name'] = name
    args['articles'] = page_obj

    return TemplateResponse(request, template_name, args)


def category(request, category_id, template_name="artigos/pages/category.html"):
    articles_db = get_list_or_404(Article.objects.filter(
        category__id=category_id, is_published=True).order_by('-id'))
    articles = articles_db
    args = {}
    args['name'] = "Cesar Luiz Ferracin"
    args['articles'] = articles
    args['title'] = f'{articles[0].category.name} - Category | '
    return TemplateResponse(request, template_name, args)


def article(request, id):
    article = get_object_or_404(Article, pk=id, is_published=True)
    args = {}
    args['name'] = "Cesar Luiz Ferracin"
    args['article'] = article
    args['is_detail_page'] = True
    return render(request, 'artigos/pages/artigo-view.html', args)


def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    articles = Article.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    return render(request, 'artigos/pages/search.html', {
        'page_title': f'Pesquisa por "{search_term}" |',
        'search_term': search_term,
        'articles': articles,
    })
