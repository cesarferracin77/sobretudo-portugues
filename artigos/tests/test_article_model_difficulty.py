from django.core.exceptions import ValidationError

from .test_article_base import ArticleTestBase


class DifficultyModelTest(ArticleTestBase):
    def setUp(self) -> None:
        self.difficulty = self.make_difficulty(difficulty='Difficulty Testing')
        return super().setUp()

    def test_difficulty_string_representation(self):
        self.assertEqual(str(self.difficulty),
                         self.difficulty.difficulty)

    def test_article_difficulty_model_name_max_length_is_65_chars(self):
        self.difficulty.difficulty = 'A' * 66
        with self.assertRaises(ValidationError):
            self.difficulty.full_clean()
