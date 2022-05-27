from artigos import views
from django.urls import resolve, reverse

from .test_article_base import ArticleTestBase


class ArticleCategoryViewTest(ArticleTestBase):

    """Testing Category page view"""

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

    def test_article_category_template_loads_articles(self):
        needed_title = 'This is a Category Test'
        # Create 1 article for testing...
        self.make_article(title=needed_title)
        # Load a homepage with the created article
        response = self.client.get(reverse('articles:category', args=(1,)))
        # Decode the content to the "utf-8" standard for searchings
        content = response.content.decode('utf-8')
        self.assertIn(needed_title, content)

    def test_article_category_template_dont_load_articles_not_published(self):
        """Test article is_published - if False dont show"""
        # Create 1 article not published for testing...
        article = self.make_article(is_published=False)
        # Load a homepage with the created article
        response = self.client.get(
            reverse('articles:article', kwargs={'id': article.category.id}))
        # Decode the content to the "utf-8" standard for searchings
        self.assertEqual(response.status_code, 404)
