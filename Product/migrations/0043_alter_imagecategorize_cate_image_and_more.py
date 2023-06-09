# Generated by Django 4.1.3 on 2023-03-09 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0042_alter_product_categorize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecategorize',
            name='cate_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagecate', to='Product.categorize_products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categorize',
            field=models.CharField(choices=[('Digital', 'کالای دیجیتال'), ('Phone', 'موبایل'), ('Appliances', 'لوازم خانگی'), ('Pooshak', 'پوشاک'), ('System', 'لپ تاپ'), ('System', 'تلوزیون'), ('Refrigerator', 'لباسشویی'), ('Headset', 'هندزفری و هدست'), ('Bag', 'کیف'), ('Cover', 'کاور'), ('Oven', 'اجاق گاز'), ('Scarf', 'روسری شال'), ('Shoes', 'کفش'), ('Manteu', 'مانتو'), ('Coat', 'پالتو')], default='Digital', max_length=20),
        ),
    ]
