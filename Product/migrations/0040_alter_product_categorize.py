# Generated by Django 4.1.3 on 2023-03-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0039_alter_product_categorize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categorize',
            field=models.CharField(choices=[('Digital', 'کالای دیجیتال'), ('va', 'hggg'), ('Digital', 'کالای دیجیتال'), ('Phone', 'موبایل'), ('Appliances', 'لوازم خانگی'), ('Laundry', 'لباسشویی'), ('Pooshak', 'پوشاک'), ('System', 'لپ تاپ'), ('System', 'تلوزیون'), ('Refrigerator', 'لباسشویی'), ('Headset', 'هندزفری و هدست'), ('Bag', 'کیف'), ('Cover', 'کاور'), ('Oven', 'اجاق گاز'), ('Scarf', 'روسری شال'), ('Shoes', 'کفش'), ('Manteu', 'مانتو'), ('Coat', 'پالتو')], default='Digital', max_length=20),
        ),
    ]
