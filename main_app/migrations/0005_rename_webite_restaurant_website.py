# Generated by Django 4.0.3 on 2022-04-01 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_style_restaurant_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='webite',
            new_name='website',
        ),
    ]