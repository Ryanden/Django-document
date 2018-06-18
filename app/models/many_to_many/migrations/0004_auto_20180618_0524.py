# Generated by Django 2.0.6 on 2018-06-18 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0003_auto_20180618_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='recommender',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]