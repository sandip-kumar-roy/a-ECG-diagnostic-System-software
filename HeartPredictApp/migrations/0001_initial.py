# Generated by Django 4.1.3 on 2022-12-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='predict_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField()),
                ('Chest_pain_type', models.CharField(max_length=50)),
                ('resting_blood_pressure', models.IntegerField()),
                ('serum_cholestoral', models.IntegerField()),
                ('fasting_blood_sugar', models.CharField(max_length=50)),
                ('resting_electrocardiographic', models.CharField(max_length=50)),
                ('max_heart_rate', models.IntegerField()),
                ('exercise_induced_angina', models.ImageField(upload_to='pics')),
                ('oldpeak', models.IntegerField()),
                ('peak_ST_segment_slope', models.CharField(max_length=50, null=True)),
                ('major_vessels', models.IntegerField(null=True)),
                ('thal', models.CharField(max_length=50, null=True)),
                ('Gender', models.CharField(max_length=50)),
            ],
        ),
    ]
