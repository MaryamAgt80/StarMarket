# Generated by Django 4.1.3 on 2023-02-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0033_alter_system_size_screen_alter_system_webcam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
    ]
