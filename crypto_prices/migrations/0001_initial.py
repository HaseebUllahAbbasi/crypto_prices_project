# Generated by Django 5.0.3 on 2024-03-21 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('value', models.DecimalField(decimal_places=10, max_digits=20)),
                ('crypto_prices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto_prices.cryptoprice')),
            ],
        ),
    ]
