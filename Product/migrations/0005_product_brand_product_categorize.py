# Generated by Django 4.1.3 on 2023-02-01 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_detailproduct_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='categorize',
            field=models.CharField(choices=[('Pooshak', 'Poshak'), ('Digital', 'Digital'), ('Appliances', 'Appliances')], default='Digital', max_length=20),
        ),
    ]
