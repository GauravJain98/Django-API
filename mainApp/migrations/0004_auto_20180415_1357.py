# Generated by Django 2.0.1 on 2018-04-15 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20180415_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='incart',
            name='product',
        ),
        migrations.DeleteModel(
            name='inCart',
        ),
    ]
