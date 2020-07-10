import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from coefficients.models import Coefficient, CommerceValue


class Command(BaseCommand):
    help = 'Seed coefficient table for testing and development.'

    def add_arguments(self, parser):
        parser.add_argument('--number', type = int)

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        self.run_seed(options['number'])
        self.stdout.write('Done.')

    def run_seed(self, number):
        """ Seed coefficient table """

        self.stdout.write("Deleting Coefficient instances")
        self.clear_data()

        for i in range(number):
            self.create_coefficient()


    def clear_data(self):
        """Delete all the table data"""

        Coefficient.objects.all().delete()

    def create_coefficient(self):
        """ Create Coefficient with random params """

        self.stdout.write('Creating coefficient...')

        coefficient = Coefficient(
            amount=random.randint(5, 45),
            percent = round(random.uniform(0, 1), 3),
            commerce_value = CommerceValue.objects.random()
        )

        coefficient.save()

        self.stdout.write("{} coefficient created.".format(coefficient))

        return coefficient