# Generated by Django 4.1.3 on 2023-02-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0034_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AddField(
            model_name='comment',
            name='lname',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
