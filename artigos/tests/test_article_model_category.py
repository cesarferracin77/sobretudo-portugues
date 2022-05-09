from django.core.exceptions import ValidationError

from .test_article_base import ArticleTestBase


class CategoryModelTest(ArticleTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Category Testing')
        return super().setUp()

    def test_article_category_string_representation(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_article_category_model_name_max_length_is_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
