# Generated by Django 2.2.3 on 2019-07-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallMarket', '0004_auto_20190708_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='goodNumber',
            field=models.IntegerField(default=1),
        ),
    ]