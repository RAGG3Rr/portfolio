# Generated by Django 4.2.1 on 2023-05-19 15:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(validators=[django.core.validators.EmailValidator()])),
                ('message', models.TextField()),
            ],
        ),
    ]
