# Generated by Django 4.1.1 on 2022-10-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_mechanicservice_hour_alter_mechanicservice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanicservice',
            name='am',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='mechanicservice',
            name='min',
            field=models.TimeField(null=True),
        ),
    ]
