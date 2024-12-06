from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['GET'])
    def out_of_stock(self, request):
        out_of_stock_products = Product.objects.filter(stock_quantity=0)
        serializer = self.get_serializer(out_of_stock_products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def update_stock(self, request, pk=None):
        product = self.get_object()
        quantity = request.data.get('quantity', 0)
        
        try:
            quantity = int(quantity)
        except ValueError:
            return Response(
                {"error": "Invalid quantity"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        product.stock_quantity += quantity
        product.save()
        
        serializer = self.get_serializer(product)
        return Response(serializer.data)