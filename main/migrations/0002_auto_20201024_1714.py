# Generated by Django 3.1.2 on 2020-10-24 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesmodel',
            options={'verbose_name': 'Картинка товара', 'verbose_name_plural': 'Картинки товаров'},
        ),
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='code',
        ),
    ]
