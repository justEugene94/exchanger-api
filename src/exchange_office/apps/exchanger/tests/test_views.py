from django.test import TestCase


class HomePageTest(TestCase):
    """ test home page"""

    def test_uses_home_template(self):
        """test: uses home template """

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'exchanger/home.html')