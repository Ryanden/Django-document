# Generated by Django 2.0.6 on 2018-06-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0010_auto_20180619_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='relation_type',
            field=models.CharField(choices=[('f', 'Follow'), ('b', 'Block')], max_length=1),
        ),
    ]
