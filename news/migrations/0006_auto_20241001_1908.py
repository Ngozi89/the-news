# Generated by Django 3.2.23 on 2024-10-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_post_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.TextField(default=None, max_length=1040),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.TextField(default=None, max_length=250),
        ),
    ]
