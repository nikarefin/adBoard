# Generated by Django 5.0.1 on 2024-01-15 22:33

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_ad_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='content',
            field=tinymce.models.HTMLField(default='Ваш контент'),
        ),
    ]
