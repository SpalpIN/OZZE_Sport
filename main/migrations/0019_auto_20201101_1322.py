# Generated by Django 3.1.2 on 2020-11-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_ordermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='details',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='shipping_by',
            field=models.CharField(max_length=11),
        ),
    ]
