# Generated by Django 3.2.4 on 2021-06-22 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0003_auto_20210620_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexprice',
            name='priceChangePercentage',
        ),
    ]
