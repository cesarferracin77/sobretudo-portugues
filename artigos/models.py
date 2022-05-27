from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.name


class Difficulty(models.Model):
    difficulty = models.CharField(max_length=65)
    units = models.IntegerField()

    def __str__(self) -> str:
        return self.difficulty


class Article(models.Model):
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=190)
    slug = models.SlugField(unique=True)
    difficulty = models.ForeignKey(
        Difficulty, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    text_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='articles/covers/%Y/%m/%d/', blank=True, null=True,
        default='articles/covers/%Y/%m/%d/default_article_cover.jpg')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    link = models.URLField(max_length=250, null=True)

    def __str__(self) -> str:
        return self.title
