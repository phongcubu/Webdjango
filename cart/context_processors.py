from django.shortcuts import render
# from .models import Order, OrderItem
#
# def counter(request):
#     try:
#         if request.user.is_authenticated:
#             cart_items = OrderItem.objects.filter(user=request.user)
#
#             cart_count = sum([cart_item.quantity for cart_item in cart_items])
#     except Order.DoesNotExist:
#         cart_count = 0
#     return dict(cart_count=cart_count)
