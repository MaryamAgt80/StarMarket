# Generated by Django 4.1.3 on 2023-03-15 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0048_brandproduct_remove_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand_p',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_product', to='Product.brandproduct'),
        ),
    ]
