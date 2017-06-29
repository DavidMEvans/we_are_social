# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from unittest import TestCase


class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)


from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Subject


class SubjectPageTest(TestCase):
    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects':
                                                               Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)


class HomePageTest(TestCase):
    fixtures = ['subjects']
