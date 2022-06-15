from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print (serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content - title
        serializer.save(content=content)
        #send a Django signal

product_list_create_view = ProductListCreateAPIView.as_view()
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_Failed  = 'pk
    #PRoduct.objects.get
product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
product_list_view = ProductListAPIView.as_view()

@api_view(['GET', 'POST'])
def product_alt_view(request, *args, **kwargs):
    method = request.method

    if method == "GET":
        pass
        #url_args??
        #get request ->detail view
        #list view
        if method == "POST":
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                # instance = serializer.save()
                print(serializer.data)
                return Response(serializer.data)
