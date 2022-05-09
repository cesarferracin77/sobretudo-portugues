from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_article_base import Article, ArticleTestBase


class ArticleModelTest(ArticleTestBase):
    def setUp(self) -> None:
        self.article = self.make_article(title='Article Testing')
        return super().setUp()

    def make_articles_no_default(self):
        article = Article(
            title='Artigo Teste',
            description='Descrição do artigo teste.',
            slug='artigo-teste',
            text='Este é o texto completo do artigo teste',
            link="http://www.uol.com.br",
            difficulty=self.make_difficulty(difficulty='Difícil', units=3),
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(
                username='tesUser', first_name='Eusou', last_name='Umteste'),
        )
        article.full_clean()
        article.save()
        return article

    @parameterized.expand([
        ('title', 90),
        ('description', 190),
        ('link', 90),
    ])
    def test_article_fields_max_length(self, field, max_length):
        setattr(self.article, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.article.full_clean()

    def test_article_text_is_html_false_by_default(self):
        article = self.make_articles_no_default()
        article.full_clean()
        article.save()
        self.assertFalse(article.text_is_html,
                         msg='Article text_is_html is not False.')

    def test_article_is_published_false_by_default(self):
        article = self.make_articles_no_default()
        article.full_clean()
        article.save()
        self.assertFalse(article.is_published,
                         msg='Article is_published is not False.')

    def test_article_string_representation(self):
        self.assertEqual(
            str(self.article),
            self.article.title,
            msg=f'Article str representation must be "{self.article.title}" but is "{str(self.article)}"'
        )
