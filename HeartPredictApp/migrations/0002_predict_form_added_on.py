# Generated by Django 4.1.3 on 2022-12-31 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartPredictApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predict_form',
            name='added_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
