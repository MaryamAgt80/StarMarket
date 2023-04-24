# Generated by Django 4.1.3 on 2023-03-16 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Site_App', '0009_messagetoadmin_is_ready'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminToUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='پاسخ')),
                ('admin_po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_massege', to=settings.AUTH_USER_MODEL, verbose_name='ادمین')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_message', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پاسخ',
                'verbose_name_plural': 'پاسخ ها',
            },
        ),
    ]