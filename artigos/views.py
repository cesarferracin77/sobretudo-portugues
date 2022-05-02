from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse
from utils.artigos.factory import make_article

from artigos.models import Article


# Create your views here.
def home(request, template_name="artigos/pages/home.html"):
    articles_db = Article.objects.filter(is_published=True).order_by('-id')
    articles = articles_db
    args = {}
    name = "Cesar Luiz Ferracin"
    args['name'] = name
    articles = articles_db
    args['articles'] = articles
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
