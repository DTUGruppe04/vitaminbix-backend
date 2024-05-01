from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, response
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from users_app.models import UserOrder
from vitaminbix import settings


# Create your views here.
@csrf_exempt
def add_user_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_order = UserOrder(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            country=data['country'],
            city=data['city'],
            zipcode=data['zipcode'],
            address1=data['address1'],
            address2=data['address2'],
            order_date=timezone.now())
        user_order.save()
        send_mail(
            "Purchase complete",
            "Thank you for you for your order!",
            settings.EMAIL_HOST_USER,
            [user_order.email],
            fail_silently=False,
        )
        return HttpResponse('user order added successfully!')
    else:
        return HttpResponse('Invalid Request', status=400)

def get_user_orders(request):
    user_orders = UserOrder.objects.all()
    user_order_list_serialized = serializers.serialize('json', user_orders)
    return JsonResponse(user_order_list_serialized, safe=False)