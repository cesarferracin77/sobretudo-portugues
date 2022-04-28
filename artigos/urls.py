from django.urls import path

from . import views

# articles:article
app_name = 'articles'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/category/<int:category_id>/', views.category, name='category'),      
    path('articles/<int:id>/', views.article, name='article'),       
]
