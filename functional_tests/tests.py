from django.http import HttpRequest
from django.test import TestCase
from blog.views import post_list


class WebTest(TestCase):

    def test_web(self):
        request = self.client.get('127.0.0.1:8000/blog/')

        request2 = HttpRequest()

        response = post_list(request)

        request.GET['page']
        response

