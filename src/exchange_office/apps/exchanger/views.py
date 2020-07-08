import json
from urllib.request import urlopen

from rest_framework.decorators import api_view
from rest_framework.response import Response

from currencies.models import Currency
from purchases.models import Purchase
from coefficients.models import Coefficient


@api_view(['GET'])
def index(request):
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    json_url = urlopen(url)

    data = json.loads(json_url.read())

    for course in data:

        if course['ccy'] != 'BTC':
            currency = Currency.objects.get(name=course['ccy'])

            sale_purchases = Purchase.objects.get_sum(currency, 'sale')
            buy_purchases = Purchase.objects.get_sum(currency, 'buy')

            coefficient_for_sale = Coefficient.objects.get_by_sum_of_purchase_amount(sale_purchases, 'sale')
            coefficient_for_buy = Coefficient.objects.get_by_sum_of_purchase_amount(buy_purchases, 'buy')

            if coefficient_for_sale:
                course['sale'] = str(round(float(course.get('sale')) * coefficient_for_sale, 5))

            if coefficient_for_buy:
                course['buy'] = str(round(float(course.get('buy')) * coefficient_for_buy, 5))

            # return Response(course['ccy'])

    return Response(data)
