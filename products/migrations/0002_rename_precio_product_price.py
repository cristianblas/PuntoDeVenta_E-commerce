# Generated by Django 4.0.1 on 2022-04-13 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='precio',
            new_name='price',
        ),
    ]
