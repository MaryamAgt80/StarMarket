# Generated by Django 4.1.3 on 2023-03-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0037_alter_categorize_products_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categorize',
            field=models.CharField(choices=[('Digital', 'کالای دیجیتال'), ('va', 'hggg')], default='Digital', max_length=20),
        ),
    ]
