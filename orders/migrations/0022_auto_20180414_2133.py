# Generated by Django 2.0.3 on 2018-04-14 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20180414_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='steakcheesetopping',
            name='pizzaTopping',
        ),
        migrations.DeleteModel(
            name='SteakCheeseTopping',
        ),
    ]
