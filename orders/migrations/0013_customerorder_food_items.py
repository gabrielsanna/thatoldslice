# Generated by Django 2.0.3 on 2018-04-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20180410_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='food_items',
            field=models.ManyToManyField(blank=True, related_name='included_in_order', to='orders.Entree'),
        ),
    ]
