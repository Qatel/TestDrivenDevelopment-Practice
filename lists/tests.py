
from django.urls import resolve
from django.test import TestCase
from django.http import HttpResponse

from lists.views import home_page
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view (self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    def home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.docode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

# Create your tests here.

# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1+1, 45)