# Generated by Django 5.0.1 on 2024-01-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_alter_ad_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='content',
            field=models.TextField(),
        ),
    ]
