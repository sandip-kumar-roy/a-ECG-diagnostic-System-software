# Generated by Django 4.1.3 on 2023-01-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locate_city',
            name='occupation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='locate_city',
            name='address',
            field=models.TextField(null=True),
        ),
    ]