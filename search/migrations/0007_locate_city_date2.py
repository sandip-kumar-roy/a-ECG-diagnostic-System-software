# Generated by Django 4.1.3 on 2023-01-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_locate_city_date1'),
    ]

    operations = [
        migrations.AddField(
            model_name='locate_city',
            name='date2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
