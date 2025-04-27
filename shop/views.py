from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import categories, shopitems, cartitems, statuses, orders, orderitems

def shop(request):
    """Главная страница магазина - отображает каталог товаров"""
    assert isinstance(request, HttpRequest)  # Проверка типа запроса
    return render(
        request, 'shop/index.html',
        {
            'title':'Каталог',
            'categories':categories.objects.all(),  # Все категории товаров
            'staff':request.user.is_staff,  # Является ли пользователь сотрудником
            'year':datetime.now().year,  # Текущий год для подвала сайта
        }
    )

def shopitem_detail(request, n):
    """Страница деталей конкретного товара"""
    shopitem = get_object_or_404(shopitems, id = n)  # Получаем товар или 404
    assert isinstance(request, HttpRequest)
    return render(
        request, 'shop/shopitem_detail.html',
        {
            'title':shopitem.name,  # Название товара как заголовок страницы
            'item':shopitem,  # Сам объект товара
            'staff':request.user.is_staff,
            'year': datetime.now().year,
        }
    )

def cart(request):
    """Страница корзины пользователя"""
    if not request.user.is_authenticated:  # Проверка авторизации
        return redirect('login')
    
    # Получаем товары в корзине текущего пользователя
    cart_items = cartitems.objects.filter(user = request.user)
    # Считаем общую стоимость товаров в корзине
    total_price = sum(item.shopitem.price * item.quantity for item in cart_items)
    
    # Обработка POST-запроса (оформление заказа)
    if request.method == 'POST':
        if not cart_items:  # Если корзина пуста
            return redirect('cart')
        # Получаем статус "Новый" для заказа
        status = statuses.objects.get(name = 'Новый')
        # Создаем заказ
        order = orders.objects.create(user = request.user, total_price = total_price, status = status)
        # Переносим товары из корзины в заказ
        for item in cart_items:
            orderitems.objects.create(
                order = order,
                shopitem = item.shopitem,
                quantity = item.quantity,
                fixed_price = item.shopitem.price  # Фиксируем цену на момент заказа
            )
        cart_items.delete()  # Очищаем корзину
        return redirect('order_detail', n = order.id)  # Переход на страницу заказа

    return render(
        request, 'shop/cart.html',
        {
            'title':'Корзина',
            'cart_items': cart_items,  # Товары в корзине
            'total_price': total_price,  # Общая сумма
            'year': datetime.now().year,
        }
    )

def history(request):
    """Страница истории заказов пользователя"""
    if not request.user.is_authenticated:
        return redirect('login')
    assert isinstance(request, HttpRequest)
    return render(
        request, 'shop/history.html',
        {
            'title':'История заказов',
            # Заказы пользователя, отсортированные по дате (новые сначала)
            'orderlist': orders.objects.filter(user = request.user).order_by('-order_date'),
            'staff':request.user.is_staff,
            'year': datetime.now().year,
        }
    )

def order_detail(request, n):
    """Страница деталей конкретного заказа"""
    if not request.user.is_authenticated:
        return redirect('login')
    order = get_object_or_404(orders, id = n)  # Получаем заказ или 404
    assert isinstance(request, HttpRequest)
    return render(
        request, 'shop/order_detail.html',
        {
            'title': order,  # Заголовок - представление заказа
            'order': order,  # Объект заказа
            'order_items': orderitems.objects.filter(order = order),  # Товары в заказе
            'staff':request.user.is_staff,
            'year': datetime.now().year,
        }
    )

def cart_add(request, n):
    """Добавление товара в корзину"""
    shopitem = get_object_or_404(shopitems, id = n)  # Получаем товар
    quantity = int(request.POST.get('quantity', 1))  # Количество из POST-запроса
    
    # Получаем или создаем запись в корзине для этого товара
    cart_item, created = cartitems.objects.get_or_create(user = request.user, shopitem = shopitem)
    
    if created:
        cart_item.quantity = quantity  # Устанавливаем количество для нового товара
    else:
        cart_item.quantity += quantity  # Увеличиваем количество существующего товара
    cart_item.save()
    return redirect('cart')  # Перенаправляем в корзину

def cart_delete(request, n):
    """Удаление товара из корзины"""
    cart_item = get_object_or_404(cartitems, id = n)
    # Проверяем, что товар принадлежит текущему пользователю
    if cart_item.user == request.user:
        cart_item.delete()  # Удаляем товар

    return redirect('cart')

def cart_update(request, n):
    """Обновление количества товара в корзине"""
    cart_item = get_object_or_404(cartitems, id = n)
    if cart_item.user == request.user:
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity  # Обновляем количество
            cart_item.save()
        else:
            cart_item.delete()  # Удаляем если количество <= 0

    return redirect('cart')
