# Generated by Django 2.0.3 on 2018-04-14 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20180414_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='SteakCheeseTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.5, max_digits=5)),
                ('pizzaTopping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaTopping')),
            ],
        ),
    ]
