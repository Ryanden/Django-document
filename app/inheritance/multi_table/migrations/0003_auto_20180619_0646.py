# Generated by Django 2.0.6 on 2018-06-19 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multi_table', '0002_supplier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['name']},
        ),
    ]
