# Generated by Django 4.1.3 on 2023-02-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_comment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system',
            name='date_create',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
