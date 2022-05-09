from django.contrib import admin

from .models import Article, Category, Difficulty


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...


class DifficultyAdmin(admin.ModelAdmin):
    ...


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

admin.site.register(Difficulty, DifficultyAdmin)
