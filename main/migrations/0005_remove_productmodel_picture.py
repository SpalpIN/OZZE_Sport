# Generated by Django 3.1.2 on 2020-10-24 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201024_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='picture',
        ),
    ]
