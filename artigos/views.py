from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from utils.artigos.factory import make_article

from artigos.models import Article


# Create your views here.
def home(request, template_name="artigos/pages/home.html"):
    articles_db = Article.objects.filter(is_published=True).order_by('-id')
    args = {}
    articles = articles_db
    args['articles'] = articles
    return TemplateResponse(request, template_name, args)

def category(request, category_id, template_name="artigos/pages/category.html"):
    articles_db = Article.objects.filter(
        category__id=category_id, 
        is_published=True
        ).order_by('-id')
    args = {}
    articles = articles_db
    args['articles'] = articles
    return TemplateResponse(request, template_name, args)

# Create your views here.
def article(request, id):
    args = {}
    name = "Cesar Luiz Ferracin"
    args['name'] = name
    args['article'] = make_article()
    args['is_detail_page'] = True
    return render(request, 'artigos/pages/artigo-view.html', args)
