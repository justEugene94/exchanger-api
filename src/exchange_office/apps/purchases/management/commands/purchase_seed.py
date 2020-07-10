import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from purchases.models import Customer, Purchase
from currencies.models import Currency


class Command(BaseCommand):
    help = "Seed customers and purchases tables for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--customers', type=int)
        parser.add_argument('--purchases', type=int)

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        self.run_seeds(options['customers'], options['purchases'])
        self.stdout.write('Done.')

    def run_seeds(self, customers, purchases):
        """Seed customers and purchases tables"""

        self.stdout.write("Deleting old instances")
        self.clear_data()

        self.stdout.write('...')
        self.stdout.write('...')
        self.stdout.write('...')

        for i in range(customers):
            self.create_customer()

        self.stdout.write('...')
        self.stdout.write('...')
        self.stdout.write('...')

        for i in range(purchases):
            self.create_purchase()

    def clear_data(self):
        """Delete all the table data"""

        Purchase.objects.all().delete()
        Customer.objects.all().delete()

    def create_customer(self):
        """Create Customer with random params"""

        self.stdout.write('Creating Customer...')

        first_names = ('John', 'Andy', 'Joe', 'Bob', 'Patrick')
        last_names = ('Johnson', 'Smith', 'Williams', 'Green', 'Black')

        customer = Customer(
            first_name=random.choice(first_names),
            last_name=random.choice(last_names),
            phone_number=random.randint(80930000000, 80939999999)
        )

        customer.save()

        self.stdout.write("{} customer created.".format(customer))

        return customer


    def create_purchase(self):
        """Create Purchases with random params"""

        self.stdout.write('Creating Purchase...')

        currency = Currency.objects.random()
        exchange_currency = Currency.objects.random()

        while currency.id == exchange_currency.id:
            exchange_currency = Currency.objects.random()
            self.stdout.write('Changing currency for purchase...')

        purchase = Purchase(
            customer=Customer.objects.random(),
            currency=currency,
            exchange_currency=exchange_currency,
            value=random.randint(100, 2000)
        )

        purchase.save()

        self.stdout.write("{} customer created.".format(purchase))

        return purchase