# Generated by Django 4.1.3 on 2023-02-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0032_remove_phone_version_system_alter_bag_suitable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='size_screen',
            field=models.CharField(max_length=100, verbose_name='اندازه صفحه'),
        ),
        migrations.AlterField(
            model_name='system',
            name='webcam',
            field=models.CharField(default='دارد', max_length=100, verbose_name='وبکم'),
        ),
    ]
