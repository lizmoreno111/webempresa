# Generated by Django 3.0.6 on 2020-05-25 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='update',
            new_name='updated',
        ),
    ]