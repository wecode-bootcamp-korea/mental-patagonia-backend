# Generated by Django 3.0.6 on 2020-06-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200616_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorproduct',
            name='image_url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='colorproductimage',
            name='image_url',
            field=models.URLField(max_length=500),
        ),
    ]