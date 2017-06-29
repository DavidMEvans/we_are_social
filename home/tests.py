from django.test import TestCase

# Create your tests here.
from unittest import TestCase


class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)


from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve


class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)



from django.shortcuts import render_to_response

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html").content
        self.assertEqual(home_page.content, home_page_template_output)


from accounts.models import User


class HomePageTest(TestCase):
    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='letmein')
        self.assertEqual(self.login, True)

    ...

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html", {'user': self.user}).content
        self.assertEqual(home_page.content, home_page_template_output)
