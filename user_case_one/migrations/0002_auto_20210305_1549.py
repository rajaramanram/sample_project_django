# Generated by Django 3.1.2 on 2021-03-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('four_table_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usage_log',
            name='First_api_call',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='usage_log',
            name='Last_api_call',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='usage_log',
            name='Month',
            field=models.CharField(max_length=256),
        ),
    ]
