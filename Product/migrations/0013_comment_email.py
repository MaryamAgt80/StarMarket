# Generated by Django 4.1.3 on 2023-02-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0012_system_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
    ]
