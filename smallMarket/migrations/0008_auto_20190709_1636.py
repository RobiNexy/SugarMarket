# Generated by Django 2.2.3 on 2019-07-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallMarket', '0007_remove_orderitem_goodtotalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='goodNumber',
            field=models.IntegerField(default=0),
        ),
    ]
