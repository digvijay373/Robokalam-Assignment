# Generated by Django 4.1.5 on 2023-01-14 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_assignment', '0002_info_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='email_address',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
