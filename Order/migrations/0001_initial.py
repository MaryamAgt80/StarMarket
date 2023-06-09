# Generated by Django 4.1.3 on 2023-02-05 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0014_remove_system_date_create_comment_date_comment_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useraddress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(0, 'پرداخت نشده'), (1, 'پرداخت شده'), (2, 'ارسال شده'), (3, 'دریافت شده')], default=0, max_length=100)),
                ('created_date', models.DateField(auto_now=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderaddres', to='Order.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userorder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetilOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('detail_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.detailproduct')),
                ('order_main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productorder', to='Product.product')),
            ],
        ),
    ]
