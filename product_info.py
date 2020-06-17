import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patagonia.settings")
django.setup()

from product.models import Color,Product

CSV_PATH_PRODUCTS = '/home/godaeyong/2차프로젝트/mental-patagonia-backend/scrapped_info/each_prod_info.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        name        = row[0]
        overview    = row[4]
        feature     = row[5]
        material   = row[6]
        Product.objects.create(name=name, overview=overview, feature=feature, materials=material)
