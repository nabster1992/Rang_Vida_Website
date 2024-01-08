import json
import stripe
from django.conf import settings
from django.http import JsonResponse
from cart.cart import Cart
#within cart app, within cart.py import Cart class
from .models import Order, OrderItem

# Creat

def start_order(request):
    cart = Cart(request)
    data = json.loads(request.body)
    total_price = 0

    items = []

    for item in cart:
        product = item['product']
        total_price += product.price * int(item['quantity'])

        

        items.append({
            'price_data': {
                'currency': 'pkr',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': product.price,
            },
            'quantity': item['quantity']
        })


    session = ''
    payment_intent = ''

    stripe.api_key = settings.STRIPE_KEY_API_HIDDEN
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/cart/success/',
        cancel_url ='http://127.0.0.1:8000/cart/',
    )

    payment_intent = session.payment_intent

    order = Order.objects.\
    create(user=request.user,
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            address1=data['address1'],
            address2=data['address2'],
            place=data['place'],
            phone=data['phone'],
            payment_intent = payment_intent,
            paid = True,
            paid_amount = total_price )

    for item in Cart(request):
        # this is the Cart class from cart.py
        product = item['product']
        quantity = int(item['quantity'])
        price = product.price * quantity

    
        item  = OrderItem.objects.create\
            (order=order,
            product=product,
            price=price,
            quantity=quantity)
        
    cart.clear()
        
    return JsonResponse({'session': session, 'order': payment_intent})

