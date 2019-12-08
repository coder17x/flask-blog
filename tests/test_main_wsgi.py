# -*- encoding: utf-8 -*-
import unittest


class BaseTestMainWsgi(unittest.TestCase):
    """Базовые тесты main_wsgi.py"""

    def setUp(self):
        from main_wsgi import app
        self.test_app = app.test_client()

    def test_for_smoke(self):
        """Обращение к корню сайта возвращает код 200"""
        response = self.test_app.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
