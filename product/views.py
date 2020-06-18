from django.shortcuts import render
from django.http    import JsonResponse,HttpResponse
from django.views   import View

from .models import (Product,
                     ProductSize,
                     ColorProduct,
                     ColorProductImage,
                     Color,
                     Fitness,
                     Size,
                     SimilarProduct
                    )
from django.db.models import Avg, Count, Q

class ProductView(View):
    def get(self, request):
        offset = int(request.GET.get('offset',0))
        limit  = int(request.GET.get('limit', 60))
        all_product = Product.objects.prefetch_related('subcategoryproduct_set','colorproduct_set','productsize_set').all()
        products=[{
            'id'                    : prod.id,
            'name'                  : prod.name,
            'price_usd'             : prod.price_usd,
            'size'                  : [{
                'id'    :   size.size.id,
                'name'  :   size.size.name,
            } for size in prod.productsize_set.all()],
            'color'                 : [{
                'name'      : color.color.name,
                'code'      : color.color.code,
                'red'       : color.color.red,
                'green'     : color.color.green,
                'blue'      : color.color.blue
            } for color in prod.colorproduct_set.all()],
            'product_image' : prod.colorproduct_set.get(is_default_image=True).image_url,
            'hover_image'   : [image.image_url for image in prod.colorproduct_set.get(is_default_image=True).colorproductimage_set.all() if image != None],
            'defalut_color' : str(prod.colorproduct_set.filter(is_default_image=True).first().color.code),
        } for prod in all_product[offset*limit : (offset+1) * limit]]


        return JsonResponse({'data':products}, status=200)

class DetailView(View):
    def get(self, request, product_id):
        try:
            product     = Product.objects.prefetch_related('review_set','colorproduct_set','productsize_set','similarproduct_set').select_related('fitness').get(id=product_id)
            product_img = product.colorproduct_set.all().prefetch_related('colorproductimage_set')
            similar_prod= product.product.annotate(aa=Avg('view_now__review__overall_rate')).all().order_by('-aa')
            product_info = {
                'id'        : product_id,
                'name'      : product.name,
                'rating'    : round(product.review_set.aggregate(Avg('overall_rate'))['overall_rate__avg'],1),
                'review'    : product.review_set.count(),
                'price_usd' : product.price_usd,
                'default'   : {
                    'id'        : product_img.get(is_default_image=True).color.id,
                    'name'      : product_img.get(is_default_image=True).color.name,
                    'code'      : product_img.get(is_default_image=True).color.code,
                    'image_url' : product_img.get(is_default_image=True).image_url,
                },
                'images'    : [{
                    'id'        : image.id,
                    'color_id'  : image.color.id,
                    'name'      : image.color.name,
                    'code'      : image.color.code,
                    'image_url' : image.image_url
                } for image in product_img],
                'option'    : [{
                    'id'            : color.color.id,
                    'color_name'    : color.color.name,
                    'color_code'    : color.color.code,
                    'main_image'    : color.image_url,
                    'sub_image'     : [{
                        'image_url' :   element.image_url
                    } for element in color.colorproductimage_set.all()]
                } for color in product_img],
                'size'      : [{
                    'id'    : element.size.id,
                    'name'  : element.size.name
                } for element in product.productsize_set.all()],
                'fitness'   : product.fitness.name,
                'overview'  : product.overview,
                'feature'   : product.feature,
                'materials' : product.materials,
                'similar'   : [{
                    'name'          : element.similar_item.name,
                    'price'         : element.similar_item.price_usd,
                    'product_image' : element.similar_item.colorproduct_set.get(is_default_image=True).image_url,
                    'hover_image'   : [prob.image_url for prob in element.similar_item.colorproduct_set.get(is_default_image=True).colorproductimage_set.all()]
                } for element in similar_prod[:5]]
            }
            return JsonResponse({'data':product_info}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({'message':'INVALID_ID'}, status=404)
        except:
            return HttpResponse(status=400)
