# Generated by Django 3.1.2 on 2020-10-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201024_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='picture',
            field=models.ImageField(default=0, upload_to='products', verbose_name='Главная картинка'),
        ),
    ]
