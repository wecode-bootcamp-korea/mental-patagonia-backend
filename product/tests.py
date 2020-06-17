from django.test import TestCase, Client

from .models import (Product,
                     Color,
                     ColorProduct,
                     ColorProductImage,
                     Fitness,
                     Review,
                     Size,
                     ProductSize
                    )

class ProductTest(TestCase):
    def setUp(self):
        client = Client()
        product1        = Product.objects.create(name="Men's Oritul Parka", overview="made in Vietnam",feature="Weight : 100g",materials="Goose, Duck", price_usd="199.99")
        color1          = Color.objects.create(name="BlueBlack",code="BLBK",red=254,green=254,blue=255)
        colorproduct1   = ColorProduct.objects.create(product=product1,color=color1,image_url="google.com",is_default_image=True)
        ColorProductImage.objects.create(color_product=colorproduct1,image_url="google.com")

    def tearDown(self):
        color1      = Color.objects.get(code="BLBK")
        product1    = Product.objects.get(name="Men's Oritul Parka")
        colorproduct= ColorProduct.objects.get(product=product1,color=color1)
        ColorProductImage.objects.get(color_product=colorproduct, image_url="google.com").delete()
        color1.delete()
        product1.delete()
        colorproduct.delete()

    def test_get_product_view(self):
        product1    = Product.objects.get(name="Men's Oritul Parka")
        response = self.client.get('/product')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(), {
            'data':[{
            "id": product1.id,
            "name": "Men's Oritul Parka",
            "price_usd": "199.99",
            "color": [
                {
                    "name": "BlueBlack",
                    "code": "BLBK",
                    "red": 254,
                    "green": 254,
                    "blue": 255
                }
            ],
            "product_image": "google.com",
            "hover_image": [
                "google.com"
            ],
            "defalut_color": "BLBK"}]})

class DetailTest(TestCase):
    def setUp(self):
        client = Client()
        fitness1        = Fitness.objects.create(name='Regulara')
        product1        = Product.objects.create(name="Men's Oritul Parka", overview="made in Vietnam",feature="Weight : 100g",materials="Goose, Duck", price_usd="199.99",fitness=fitness1)
        color1          = Color.objects.create(name="BlueBlack",code="BLBK",red=254,green=254,blue=255)
        colorproduct    = ColorProduct.objects.create(product=product1,color=color1,image_url="google.com",is_default_image=True)
        ColorProductImage.objects.create(color_product=colorproduct,image_url="google.com")
        Review.objects.create(firstname="John",email="google@gmail.com",height="6'6",product_size="M",overall_rate=4,title="This is lovely jacket",detail_review="aha",product=product1)
        size1           = Size.objects.create(name='SS')
        ProductSize.objects.create(size=size1,product=product1)



    def tearDown(self):
        color1      = Color.objects.get(code="BLBK")
        product1    = Product.objects.get(name="Men's Oritul Parka")
        colorproduct= ColorProduct.objects.get(product=product1,color=color1)
        review1     = Review.objects.get(product=product1,firstname="John",email="google@gmail.com")
        size1       = Size.objects.get(name='SS')
        ProductSize.objects.get(size=size1,product=product1).delete()
        ColorProductImage.objects.get(color_product=colorproduct, image_url="google.com").delete()
        color1.delete()
        product1.delete()
        colorproduct.delete()
        review1.delete()
        size1.delete()
        Fitness.objects.get(name="Regulara")

    def test_get_detail_view(self):
        response = self.client.get('/product/1')
        color1      = Color.objects.get(code="BLBK")
        product1    = Product.objects.get(name="Men's Oritul Parka")
        colorproduct= ColorProduct.objects.get(product=product1,color=color1)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{
            "data": {
                "id": product1.id,
                "name": "Men's Oritul Parka",
                "rating": "4.0",
                "review": 1,
                "price_usd": "199.99",
                "default":
                {
                        "id": color1.id,
                        "name": "BlueBlack",
                        "code": "BLBK",
                        "image_url": "google.com"
                },
                "images": [
                    {
                        "id": colorproduct.id,
                        "image_url": "google.com"
                    },
                ],
                "option": [
                    {
                        "id": color1.id,
                        "color_name": "BlueBlack",
                        "color_code": "BLBK",
                        "main_image": "google.com",
                        "sub_image": [
                            {
                                "image_url": "google.com"
                            }
                        ]
                    },
                ],
                "size": [
                    "SS"
                ],
                "fitness": "Regulara",
                "overview": "made in Vietnam",
                "feature": "Weight : 100g",
                "materials": "Goose, Duck"
            }
        })
    def test_get_detail_view_doesnotexist(self):
        response = self.client.get('/product/20')
        self.assertEqual(response.status_code,404)
        self.assertEqual(response.json(),{'message':'INVALID_ID'})

