from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.
def home(request, template_name="artigos/pages/home.html"):
    args = {}
    name = "Cesar Luiz Ferracin"
    args['name'] = name
    return TemplateResponse(request, template_name, args)
