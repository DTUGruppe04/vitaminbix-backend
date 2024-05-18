from django.http import JsonResponse, HttpResponse
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from product_app.models import Book
from product_app.models import Product
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


# Simple HelloWorld Endpoint Response
def hello_view(request):
    return JsonResponse({"message": "Hello Frontend. This data came from the backend. Nice to see you"})


# Add items from json
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_products(request):
    temp = open('product_app/data.json')
    data = json.load(temp)

    for i in range(len(data)):
        products = Product(data[i]['id'], data[i]['name'], data[i]['price'],
                      data[i]['currency'], data[i]['img'])
        products.save()

    return HttpResponse('Products added succesfully!', status=200)


# Return all products
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_products(request):
    products = Product.objects.all()
    product_list_serialized = serializers.serialize('json', products)
    return JsonResponse(product_list_serialized, safe=False)
