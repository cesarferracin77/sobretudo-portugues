from artigos import views
from django.urls import resolve, reverse

from .test_article_base import ArticleTestBase


class ArticleDetailViewTest(ArticleTestBase):

    """Testing Article Detail page view"""

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

    def test_article_detail_template_loads_correct_article(self):
        needed_title = 'This is a detail page - It loads one article'
        # Create 1 article for testing...
        self.make_article(title=needed_title)
        # Load a homepage with the created article
        response = self.client.get(
            reverse('articles:article', kwargs={'id': 1}))
        # Decode the content with the "utf-8" charset for searchings
        content = response.content.decode('utf-8')
        self.assertIn(needed_title, content)

    def test_article_detail_template_dont_load_article_not_published(self):
        """Test article is_published - if False dont show"""
        # Create 1 article not published for testing...
        article = self.make_article(is_published=False)
        # Load a homepage with the created article
        response = self.client.get(
            reverse('articles:article', kwargs={'id': article.id}))
        # Decode the content to the "utf-8" standard for searchings
        self.assertEqual(response.status_code, 404)
