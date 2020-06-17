import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patagonia.settings")
django.setup()

from product.models import Color, Product, Fitness

CSV_PATH_PRODUCTS = '/home/godaeyong/2차프로젝트/mental-patagonia-backend/scrapped_info/each_prod_fitness.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        A   = row[0]
        B   = row[1]
        C   = row[2]
        try:
            D   = Product.objects.get(name=A)
            E   = Fitness.objects.get(name=B)
            D.fitness   = E
            D.price_usd = C
            D.save()
        except:
            pass
