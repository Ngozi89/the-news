# Generated by Django 3.2.23 on 2024-10-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20241001_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]