# Generated by Django 2.0.3 on 2018-04-10 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_remove_customerorder_food_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealsinorder',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='pizzas', to='orders.PizzaTopping'),
        ),
    ]
