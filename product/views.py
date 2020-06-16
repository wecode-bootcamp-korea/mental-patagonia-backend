from django.shortcuts import render
from django.http    import JsonResponse
from django.views   import View
# Create your views here.

from .models import Product, ProductSize, ColorProduct, ColorProductImage, Color

class ProductView(View):
    def get(self, request):
        offset = int(request.GET.get('offset',0))
        limit  = int(request.GET.get('limit', 60))
        all_product = Product.objects.prefetch_related('subcategoryproduct_set','colorproduct_set').all()

        products=[{
            'id'                    : prod.id,
            'name'                  : prod.name,
            'price_usd'             : prod.price_usd,
            'color'                 : [{
                'name'      : color.color.name,
                'code'      : color.color.code,
                'red'       : color.color.red,
                'green'     : color.color.green,
                'blue'      : color.color.blue
            } for color in prod.colorproduct_set.all()],
            'product_image' : prod.colorproduct_set.get(is_default_image=True).image_url,
            'hover_image'   : [image.image_url for image in prod.colorproduct_set.filter(is_default_image=True) if image != None],
            'defalut_color' : str(prod.colorproduct_set.filter(is_default_image=True).first().color.code),
        } for prod in all_product[offset*limit : (offset+1) * limit]]


        return JsonResponse({'data':products}, status=200)

class MainCategoryView(View):
    def get(self, request):
        all_category    = Main
