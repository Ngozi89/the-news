# Generated by Django 3.2.23 on 2024-08-02 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='method',
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
