from rest_framework import viewsets
from tecfood_cart.models import Cart
from tecfood_cart.serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer