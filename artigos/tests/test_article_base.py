from artigos.models import Article, Category, Difficulty, User
from django.test import TestCase


class ArticleTestBase(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Categoria Teste'):
        return Category.objects.create(name=name)

    def make_difficulty(self, difficulty='Fácil', units=1):
        return Difficulty.objects.create(difficulty=difficulty, units=units)

    def make_author(
        self,
        first_name='Cesar',
        last_name='Ferracin',
        username='cferracin',
        password='1234',
        email='cesarferracin@gmail.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_article(
        self,
        title='Artigo Teste',
        description='Descrição do artigo teste.',
        slug='artigo-teste',
        text='Este é o texto completo do artigo teste',
        link="http://www.uol.com.br",
        text_is_html=False,
        is_published=True,
        difficulty_data=None,
        category_data=None,
        author_data=None,
    ):
        if difficulty_data is None:
            difficulty_data = {}

        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Article.objects.create(
            title=title,
            description=description,
            slug=slug,
            text=text,
            link=link,
            text_is_html=text_is_html,
            is_published=is_published,
            difficulty=self.make_difficulty(**difficulty_data),
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
        )
