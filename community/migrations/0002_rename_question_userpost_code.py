# Generated by Django 5.0 on 2023-12-23 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpost',
            old_name='question',
            new_name='code',
        ),
    ]
