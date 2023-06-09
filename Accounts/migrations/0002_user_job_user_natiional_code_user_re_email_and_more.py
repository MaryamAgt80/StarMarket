# Generated by Django 4.1.3 on 2023-02-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='شغل'),
        ),
        migrations.AddField(
            model_name='user',
            name='natiional_code',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='کد ملی'),
        ),
        migrations.AddField(
            model_name='user',
            name='re_email',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='ایمیل جایگزین'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
    ]
