# Generated by Django 5.0 on 2024-01-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
