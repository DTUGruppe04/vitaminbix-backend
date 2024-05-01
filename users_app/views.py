from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, response
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from users_app.models import UserOrder
from vitaminbix import settings
from product_app.models import Product


# Create your views here.
@csrf_exempt
def add_user_order(request):
    from product_app.models import Product

    if request.method == 'POST':
        data = json.loads(request.body)
        user_order = UserOrder(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            country=data['country'],
            city=data['city'],
            zipcode=data['zipcode'],
            address1=data['address1'],
            address2=data['address2'],
            order_date=timezone.now())
        user_order.save()

        product_ids = data.get('product_ids', [])
        product_details = []
        for product_id in product_ids:
            try:
                product = Product.objects.get(id=product_id)
                user_order.products.add(product)
                product_details.append(str(product))
            except Product.DoesNotExist:
                pass

        product_details_str = '\n'.join(product_details)

        send_mail(
            "Purchase complete",
            "Thank you for your order! Here are the details of your purchased products:\n" + product_details_str,
            settings.EMAIL_HOST_USER,
            [user_order.email],
            fail_silently=False,
        )
        return HttpResponse('user order added successfully!')
    else:
        return HttpResponse('Invalid Request', status=400)

def get_user_orders(request):
    user_orders = UserOrder.objects.all()
    user_order_list = []
    for user_order in user_orders:
        products = list(user_order.products.values())  # Get full product objects
        order_dict = {
            'first_name': user_order.first_name,
            'last_name': user_order.last_name,
            'email': user_order.email,
            'phone_number': user_order.phone_number,
            'country': user_order.country,
            'city': user_order.city,
            'zipcode': user_order.zipcode,
            'address1': user_order.address1,
            'address2': user_order.address2,
            'order_date': user_order.order_date,
            'products': products,
        }
        user_order_list.append(order_dict)
    return JsonResponse(user_order_list, safe=False)
