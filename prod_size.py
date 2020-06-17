import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patagonia.settings")
django.setup()

from product.models import Product, Size, ProductSize

CSV_PATH_PRODUCTS = '/home/godaeyong/2차프로젝트/mental-patagonia-backend/scrapped_info/prod_size_info.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        name    = row[0]
        size    = row[2].strip('[').strip(']').split(", ")
        real    = [ k.strip("'") for k in size]
        prod    = Product.objects.get(name=name)
        for i in real:
            x = Size.objects.get(name=i)
            ProductSize.objects.create(size=x,product=prod)


