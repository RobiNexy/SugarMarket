# Generated by Django 2.2.3 on 2019-07-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallMarket', '0005_auto_20190709_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='isInCart',
            field=models.BooleanField(default=True),
        ),
    ]
