# Generated by Django 4.1.3 on 2023-03-09 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0036_categorize_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorize_products',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subset', to='Product.categorize_products', verbose_name='زیر مجموعه:'),
        ),
    ]
