# Generated by Django 4.1.3 on 2023-02-07 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0021_delete_detailpooshak'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailPooshak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('detail_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_pooshak', to='Product.detailproduct')),
            ],
        ),
    ]