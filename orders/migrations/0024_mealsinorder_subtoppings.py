# Generated by Django 2.0.3 on 2018-04-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_steakcheesetopping'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealsinorder',
            name='subToppings',
            field=models.ManyToManyField(blank=True, related_name='subtoppings', to='orders.SteakCheeseTopping'),
        ),
    ]
