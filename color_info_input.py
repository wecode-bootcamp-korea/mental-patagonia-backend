import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patagonia.settings")
django.setup()

from product.models import Color

CSV_PATH_PRODUCTS = '/home/godaeyong/2차프로젝트/mental-patagonia-backend/scrapped_info/all_color_code_rgb.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        name    = row[0]
        code    = row[1]
        r       = row[2]
        g       = row[3]
        b       = row[4]
        Color.objects.create(name=name, code=code, red=r, green=g,blue=b)
