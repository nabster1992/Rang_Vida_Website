# Generated by Django 5.0 on 2024-01-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
