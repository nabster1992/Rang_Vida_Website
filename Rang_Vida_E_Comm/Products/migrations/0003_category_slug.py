# Generated by Django 5.0 on 2023-12-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_remove_category_slug_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
