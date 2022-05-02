from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class ArticleURLsTest(TestCase):
    def test_article_home_url_is_correct(self):
        url = reverse('articles:home')
        self.assertEqual(url, '/')

    def test_article_category_url_is_correct(self):
        url = reverse('articles:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/articles/category/1/')

    def test_article_detail_url_is_correct(self):
        url = reverse('articles:article', kwargs={'id': 1})
        self.assertEqual(url, '/articles/1/')
