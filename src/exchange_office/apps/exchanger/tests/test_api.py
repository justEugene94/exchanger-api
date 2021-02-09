from django.test import TestCase


class ExchangerApiTest(TestCase):
    """exchanger api tests"""

    def test_GET_exchange_rate(self):
        """ test GET exchange rate """

        response = self.client.get('api/')

        print(response.status_code)

        self.assertEqual(response.status_code, 200)