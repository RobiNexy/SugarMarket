# Generated by Django 2.2.3 on 2019-07-09 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smallMarket', '0006_orderitem_isincart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='goodTotalPrice',
        ),
    ]
