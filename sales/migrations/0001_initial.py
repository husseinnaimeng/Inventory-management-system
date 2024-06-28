# Generated by Django 5.0.2 on 2024-06-24 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('inventory', '0003_brand_category_manufacture_unit_inventory_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_order_item', to='customer.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('On Hold', 'On Hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Returned', 'Returned'), ('Failed', 'Failed')], default='Pending', max_length=20)),
                ('tax', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('cutomer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
                ('order_items', models.ManyToManyField(related_name='order', to='sales.orderitem')),
            ],
        ),
    ]
