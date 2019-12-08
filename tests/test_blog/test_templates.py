# -*- encoding: utf-8 -*-
import unittest

from flask import render_template


class TemplatesTestCase(unittest.TestCase):
    """Тестирование шаблонов"""

    def setUp(self):
        from main_wsgi import app
        self.test_app = app
        self.test_client = app.test_client()

    def test_index_html_without_title(self):
        """Тест рендеринга шаблона главной страницы index.html.j2 (без передачи title)"""
        index_page = ""
        is_raised = False
        try:
            with self.test_app.app_context():
                index_page = render_template("index.html.j2")
        except Exception as e:
            is_raised = True
            print(e)

        self.assertFalse(is_raised, 'Ошибка рендера шаблона')

        is_str = isinstance(index_page, str)
        self.assertTrue(is_str, 'Шаблон не является строкой')

        title_if_title_not_pass = 'New site' in index_page
        self.assertTrue(title_if_title_not_pass, 'Заголовок не "New site"')

    def test_index_html_with_title(self):
        """Тест рендеринга шаблона главной страницы index.html.j2 (с переданным title)"""
        index_page = ""
        is_raised = False
        try:
            with self.test_app.app_context():
                index_page = render_template("index.html.j2", title="Blog site")
        except Exception as e:
            is_raised = True
            print(e)

        self.assertFalse(is_raised, 'Ошибка рендера шаблона')

        is_str = isinstance(index_page, str)
        self.assertTrue(is_str, 'Шаблон не является строкой')

        title_if_title_is_pass = 'Blog site' in index_page
        self.assertTrue(title_if_title_is_pass, 'Заголовок не "Blog site"')


if __name__ == '__main__':
    unittest.main()
