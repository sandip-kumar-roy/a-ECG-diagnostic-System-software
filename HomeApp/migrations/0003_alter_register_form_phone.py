# Generated by Django 4.1.3 on 2022-12-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0002_alter_register_form_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_form',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
