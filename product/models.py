from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'main_categories'

class MainCategorySubCategory(models.Model):
    main_category = models.ForeignKey('MainCategory', on_delete=models.SET_NULL, null=True)
    sub_category  = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'main_categories_sub_categories'

class SubCategory(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'sub_categories'

class SubCategoryProduct(models.Model):
    sub_category = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
    product      = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'sub_category_products'

class Product(models.Model):
    name              = models.CharField(max_length=200)
    overview          = models.CharField(max_length=2000)
    feature           = models.CharField(max_length=2000)
    materials         = models.CharField(max_length=2000)
    fitness           = models.ForeignKey('Fitness', on_delete=models.SET_NULL, null=True)
    launch_date       = models.DateField(null=True)
    price_usd         = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    size              = models.ManyToManyField('Size', related_name='size', through='ProductSize')
    color             = models.ManyToManyField('Color', related_name='color', through='ColorProduct')

    class Meta:
        db_table = 'products'

class Review(models.Model):
    firstname     = models.CharField(max_length=45)
    email         = models.EmailField(max_length=45, null=True)
    height        = models.CharField(max_length=45, null=True)
    product_size  = models.CharField(max_length=45, null=True)
    rate_fit      = models.CharField(max_length=45, null=True)
    overall_rate  = models.DecimalField(max_digits=5, decimal_places=1)
    title         = models.CharField(max_length=200)
    detail_review = models.TextField()
    product       = models.ForeignKey('Product',on_delete=models.SET_NULL, null=True)
    use_for       = models.ManyToManyField('UseFor', related_name='use_for', through='UseforReview', null=True)
    written_date  = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'

class ProductSize(models.Model):
    size    = models.ForeignKey('Size',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'product_sizes'

class ColorProduct(models.Model):
    product             = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    color               = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    name                = models.CharField(max_length=45, null=True)
    image_url           = models.URLField(max_length=500)
    is_default_image    = models.BooleanField(default=False)

    class Meta:
        db_table = 'color_products'

class ColorProductImage(models.Model):
    image_url     = models.URLField(max_length=500)
    color_product = models.ForeignKey('ColorProduct', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'color_product_images'

class Fitness(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'fitnesses'

class SimilarProduct(models.Model):
    view_now     = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='product')
    similar_item = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'similar_products'

class UseforReview(models.Model):
    review = models.ForeignKey('Review', on_delete=models.SET_NULL, null=True)
    usefor = models.ForeignKey('UseFor', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'usefor_reviews'

class Size(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'sizes'

class Color(models.Model):
    name    = models.CharField(max_length=200)
    code    = models.CharField(max_length=45)
    red     = models.IntegerField(null=True)
    green   = models.IntegerField(null=True)
    blue    = models.IntegerField(null=True)

    class Meta:
        db_table = 'colors'

class Usefor(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'usefors'

