# Generated by Django 3.0.6 on 2020-05-26 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
    ]
