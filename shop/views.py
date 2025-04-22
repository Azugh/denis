from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import categories, shopitems, cartitems, statuses, orders, orderitems

def shop(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'shop/index.html',
        {
            'title':'Каталог',
            'categories':categories.objects.all(),
            'staff':request.user.is_staff,
            'year':datetime.now().year,
        }
    )

def shopitem_detail(request, n):
    shopitem = get_object_or_404(shopitems, id = n)
    assert isinstance(request, HttpRequest)
    return render(
        request, 'shop/shopitem_detail.html',
        {
            'title':shopitem.name,
            'item':shopitem,
            'staff':request.user.is_staff,
            'year': datetime.now().year,
        }
    )

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart_items = cartitems.objects.filter(user = request.user)
    total_price = sum(item.shopitem.price * item.quantity for item in cart_items)
    
    if request.method == 'POST':
        if not cart_items:
            return redirect('cart')
        status = statuses.objects.get(name = 'Новый')
        order = orders.objects.create(user = request.user, total_price = total_price, status = status)
        for item in cart_items:
            orderitems.objects.create(
                order = order,
                shopitem = item.shopitem,
                quantity = item.quantity,
                fixed_price = item.shopitem.price
            )
        cart_items.delete()
        return redirect('order_detail', n = order.id)

    return render(
        request, 'shop/cart.html',
        {
            'title':'Корзина',
            'cart_items': cart_items,
            'total_price': total_price,
            'year': datetime.now().year,
        }
    )

def history(request):
    if not request.user.is_authenticated:
        return redirect('login')
    assert isinstance(request, HttpRequest)
    return render(
        request, 'shop/history.html',
        {
            'title':'История заказов',
            'orderlist': orders.objects.filter(user = request.user).order_by('-order_date'),
            'staff':request.user.is_staff,
            'year': datetime.now().year,
        }
    )

def order_detail(request, n):
    if not request.user.is_authenticated:
        return redirect('login')
    order = get_object_or_404(orders, id = n)
    assert isinstance(request, HttpRequest)
    return render(
        request, 'shop/order_detail.html',
        {
            'title': order,
            'order': order,
            'order_items': orderitems.objects.filter(order = order),
            'staff':request.user.is_staff,
            'year': datetime.now().year,
        }
    )

def cart_add(request, n):
    shopitem = get_object_or_404(shopitems, id = n)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = cartitems.objects.get_or_create(user = request.user, shopitem = shopitem)
    if created:
        cart_item.quantity = quantity
    else:
        cart_item.quantity += quantity
    cart_item.save()
    return redirect('cart')

def cart_delete(request, n):
    cart_item = get_object_or_404(cartitems, id = n)
    if cart_item.user == request.user:
        cart_item.delete()

    return redirect('cart')

def cart_update(request, n):
    cart_item = get_object_or_404(cartitems, id = n)
    if cart_item.user == request.user:
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')


