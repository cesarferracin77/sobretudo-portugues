from unittest import skip

from artigos import views
from django.urls import resolve, reverse

from .test_article_base import ArticleTestBase


class ArticleViewsTest(ArticleTestBase):

    def test_article_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertTrue(True)
        self.assertIs(view.func, views.home)

    def test_article_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('articles:home'))
        self.assertEqual(response.status_code, 200)

    def test_article_home_template_loads_articles(self):
        # Create 1 article for testing...
        self.make_article(category_data={'name': 'Neologismos'})
        # Load a homepage with the created article
        response = self.client.get(reverse('articles:home'))
        # Check if one article exists
        self.assertEqual(len(response.context['articles']), 1)
        # Decode the content to the "utf-8" standard for searchings
        content = response.content.decode('utf-8')

        self.assertIn('Artigo Teste', content)
        self.assertIn('Descrição do artigo teste.', content)
        self.assertIn('Neologismos', content)
        self.assertIn('Fácil', content)
        self.assertIn('Cesar Ferracin', content)

    def test_article_home_view_loads_correct_template(self):
        response = self.client.get(reverse('articles:home'))
        self.assertTemplateUsed(response, 'artigos/pages/home.html')

    def test_article_home_shows_no_articles_found(self):
        response = self.client.get(reverse('articles:home'))
        self.assertIn(
            'No articles found',
            response.content.decode('utf-8'))

    def test_article_category_view_function_is_correct(self):
        view = resolve(
            reverse('articles:category', kwargs={'category_id': 90000})
        )
        self.assertTrue(True)
        self.assertIs(view.func, views.category)

    def test_article_category_view_returns_404_if_no_category_found(self):
        response = self.client.get(
            reverse('articles:category', kwargs={'category_id': 90000}))
        self.assertEqual(response.status_code, 404)

    def test_article_detail_view_function_is_correct(self):
        view = resolve(
            reverse('articles:article', kwargs={'id': 1})
        )
        self.assertTrue(True)
        self.assertIs(view.func, views.article)

    def test_article_detail_view_returns_404_if_no_category_found(self):
        response = self.client.get(
            reverse('articles:article', kwargs={'id': 90000}))
        self.assertEqual(response.status_code, 404)

    @skip('Testing skipping a failed test...')
    def test_skip(self):
        self.fail()
