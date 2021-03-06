# Generated by Django 3.0.5 on 2020-07-10 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='фамилия')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='номер телефона')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
                'db_table': 'customers',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(verbose_name='денежная сумма')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='currencies.Currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='purchases.Customer')),
                ('exchange_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchange_purchase', to='currencies.Currency')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
                'db_table': 'purchases',
                'ordering': ['-created_at'],
            },
        ),
    ]
