# Generated by Django 5.0.4 on 2024-06-11 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0004_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
