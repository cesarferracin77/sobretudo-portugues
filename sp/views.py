from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main_home(request):
    return render(request, 'global/home.html')
