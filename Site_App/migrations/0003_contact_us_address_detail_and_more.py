# Generated by Django 4.1.3 on 2023-03-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_App', '0002_remove_messagetoadmin_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='address_detail',
            field=models.CharField(blank=True, default=True, max_length=100, null=True, verbose_name='جزئیات ادرس'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='address_contact',
            field=models.CharField(max_length=100, verbose_name='ادرس :کشور-استان-شهر'),
        ),
    ]
