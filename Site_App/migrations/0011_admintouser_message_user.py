# Generated by Django 4.1.3 on 2023-03-16 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_App', '0010_admintouser'),
    ]

    operations = [
        migrations.AddField(
            model_name='admintouser',
            name='message_user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Site_App.messagetoadmin', verbose_name='پیام کاربر'),
        ),
    ]
