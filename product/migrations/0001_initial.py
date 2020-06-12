# Generated by Django 3.0.5 on 2020-06-15 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=45)),
                ('red', models.IntegerField(null=True)),
                ('green', models.IntegerField(null=True)),
                ('blue', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='ColorProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True)),
                ('image_url', models.CharField(max_length=500)),
                ('deault_image', models.BooleanField(default=False)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color')),
            ],
            options={
                'db_table': 'color_products',
            },
        ),
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'fitnesses',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('overview', models.CharField(max_length=2000)),
                ('feature', models.CharField(max_length=2000)),
                ('materials', models.CharField(max_length=2000)),
                ('launch_date', models.DateField(null=True)),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('color', models.ManyToManyField(related_name='color', through='product.ColorProduct', to='product.Color')),
                ('fitness', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Fitness')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45, null=True)),
                ('height', models.CharField(max_length=45, null=True)),
                ('product_size', models.CharField(max_length=45, null=True)),
                ('rate_fit', models.CharField(max_length=45, null=True)),
                ('overall_rate', models.DecimalField(decimal_places=1, max_digits=5)),
                ('title', models.CharField(max_length=200)),
                ('detail_review', models.TextField()),
                ('written_date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'sub_categories',
            },
        ),
        migrations.CreateModel(
            name='Usefor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'usefors',
            },
        ),
        migrations.CreateModel(
            name='UseforReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Review')),
                ('usefor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Usefor')),
            ],
            options={
                'db_table': 'usefor_reviews',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.SubCategory')),
            ],
            options={
                'db_table': 'sub_category_products',
            },
        ),
        migrations.CreateModel(
            name='SimilarProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('view_now', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.Product')),
            ],
            options={
                'db_table': 'similar_products',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='use_for',
            field=models.ManyToManyField(related_name='use_for', through='product.UseforReview', to='product.Usefor'),
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
            ],
            options={
                'db_table': 'product_sizes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(related_name='size', through='product.ProductSize', to='product.Size'),
        ),
        migrations.CreateModel(
            name='MainCategorySubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.MainCategory')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.SubCategory')),
            ],
            options={
                'db_table': 'main_categories_sub_categories',
            },
        ),
        migrations.CreateModel(
            name='ColorProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=500)),
                ('color_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ColorProduct')),
            ],
            options={
                'db_table': 'color_product_images',
            },
        ),
        migrations.AddField(
            model_name='colorproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product'),
        ),
    ]