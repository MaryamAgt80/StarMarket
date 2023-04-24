# Generated by Django 4.1.3 on 2023-02-09 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0034_alter_product_price'),
        ('Order', '0006_slider_in_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='detilorder',
            name='detail_pooshak',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.detailpooshak'),
        ),
        migrations.AlterField(
            model_name='detilorder',
            name='detail_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.detailproduct'),
        ),
    ]
