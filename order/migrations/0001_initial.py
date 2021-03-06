# Generated by Django 3.0.6 on 2020-06-15 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_message', models.CharField(max_length=2000)),
                ('address_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.AddressBook')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Member')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'order_status',
            },
        ),
        migrations.CreateModel(
            name='ShippingMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'shipping_methods',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
            ],
            options={
                'db_table': 'order_details',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.OrderStatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.ShippingMethod'),
        ),
    ]
