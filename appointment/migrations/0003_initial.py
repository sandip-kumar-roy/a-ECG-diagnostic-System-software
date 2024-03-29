# Generated by Django 4.1.3 on 2023-01-04 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0002_delete_create_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=250)),
                ('doctor_id', models.CharField(max_length=250)),
                ('apointment_date', models.CharField(max_length=50)),
                ('invoice_id', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('processed_on', models.DateTimeField(auto_now_add=True)),
                ('usr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
