# Generated by Django 4.1.3 on 2022-12-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_form',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
