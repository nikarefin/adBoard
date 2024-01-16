# Generated by Django 5.0.1 on 2024-01-14 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RenameField(
            model_name='response',
            old_name='user',
            new_name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
