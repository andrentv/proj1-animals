# Generated by Django 2.2 on 2021-05-12 19:44

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to='media/')),
                ('description', models.TextField(max_length=360)),
                ('difficulty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('animal', models.CharField(choices=[('Cat', 'CAT'), ('Dog', 'DOG')], max_length=3)),
                ('age', models.CharField(choices=[('Young', 'YOUNG'), ('Old', 'OLD')], max_length=5)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=6)),
                ('sheltered', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
