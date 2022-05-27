from artigos import views
from django.urls import resolve, reverse

from .test_article_base import ArticleTestBase


class ArticleSearchViewTest(ArticleTestBase):

    def test_article_search_uses_correct_view_function(self):
        resolved = resolve(reverse('articles:search'))
        self.assertIs(resolved.func, views.search)

    def test_article_search_loads_correct_template(self):
        response = self.client.get(reverse('articles:search') + '?q=teste')
        self.assertTemplateUsed(response, 'artigos/pages/search.html')

    def test_article_search_raises_404_if_no_search_term(self):
        url = reverse('articles:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_article_search_term_is_on_page_title_and_escaped(self):
        url = reverse('articles:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Pesquisa por &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )

    def test_article_search_can_find_recipe_by_title(self):
        title1 = 'This is article one'
        title2 = 'This is article two'

        article1 = self.make_article(
            slug='one', title=title1, author_data={'username': 'one'}
        )
        article2 = self.make_article(
            slug='two', title=title2, author_data={'username': 'two'}
        )

        search_url = reverse('articles:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')

        self.assertIn(article1, response1.context['articles'])
        self.assertNotIn(article2, response1.context['articles'])

        self.assertIn(article2, response2.context['articles'])
        self.assertNotIn(article1, response2.context['articles'])

        self.assertIn(article1, response_both.context['articles'])
        self.assertIn(article2, response_both.context['articles'])
