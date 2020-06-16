from django.test import TestCase, Client

from .models import Product, Color, ColorProduct,ColorProductImage

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
        response = self.client.get('/product')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(), {
            'data':[{
            "id": 1,
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
