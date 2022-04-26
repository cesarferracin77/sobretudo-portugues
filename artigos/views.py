from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from utils.artigos.factory import make_article


# Create your views here.
def home(request, template_name="artigos/pages/home.html"):
    args = {}
    name = "Cesar Luiz Ferracin"
    articles = [make_article() for _ in range(10)]
    args['name'] = name
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
