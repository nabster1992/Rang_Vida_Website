# Generated by Django 5.0 on 2024-01-08 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_alter_category_options_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='product',
        ),
    ]