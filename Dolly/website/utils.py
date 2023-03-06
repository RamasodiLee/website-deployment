import json
from tkinter import FALSE
from . models import *

def cookieCart(request):
    try:
        cart =json.loads(request.COOKIES['cart'])
    except:
               cart = {}
    print('CART:',cart)

    items =[]
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    cartItems= order['get_cart_items']
    for i in cart:
        try:
            if(cart[i]['quantity']>0):
             cartItems += cart[i]["quantity"]
            product = Product.objects.get(id=i)
            total =(product.price*cart[i]["quantity"])
               
            order['get_cart_items']+=total
            order['get_cart_total']+=cart[i]['quantity']
            item = {
                'id':product.id,
                'product':{
                'id':product.id,
                'name':product.name,
                'price':product.price,
                'imageURL':product.imageURL,
                },
                'quantity':cart[i]["quantity"],
                'digital':product.digital,'get_total':total,
               }
            items.append(item)

            if product.digital == False:
                 order['shipping']=True
        except:
            pass
    return {'cartItems':cartItems,'order':order,'items':items}

def cartData(request):
    if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=FALSE)
          items = order.orderitem_set.all()
          cartItems= order.get_cart_items
    else:
          cookieData = cookieCart()
          cartItema = cookieData['cartItems']
          order = cookieData['order']
          items = cookieData['items']
    return{'cartItems':cartItems,'order':order,'items':items}

def guestOrder(request, data):

        #  print('COOKIES:',request.COOKIES)
         name = data['form']['name']
         email = data['form']['email']

         cookieData = cookieCart(request)
         items = cookieData['items']

         customer, created = customer.objects.get_or_create(email=email)
         customer.name = name
         customer.save()

         order = order.objects.create(
               customer=customer,
               complete=False,
          )
         for item in items:
          product = product.objects.get(id=item['product']['id'])  

          orderItems = orderItems.objects.create(
               product =product,
               order=order,
               quantity=item['quantity'] if item['quantity']>0 else -1*item['quantity']
          ) 

    
         return customer,order