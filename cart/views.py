from django.shortcuts import render, redirect,get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from django.contrib import messages
from django.utils import timezone

# hiển thị sản phẩm ra trong phần giỏ hàng
@login_required(login_url='user_login') # điều kiện vào giỏ hàng phải đăng nhập
def carts(request):
    if Order.objects.filter(user=request.user, ordered=False):
        order = Order.objects.get(user=request.user,ordered=False)

        context = {
            'order': order,

         }
        return render(request, 'app/cart.html',context)

    return render(request,'app/cart.html')


#  thêm 1 sản phẩm vào giỏ hàng
def add_cart(request, pk):
    product = Product.objects.get(pk=pk) # lấy theo id
    # đặt hàng
    order_item, created = OrderItem.objects.get_or_create(
         product=product,
         user=request.user,
         ordered=False,
     )
    # lấy dữ liệu từng sản phẩm  mà khách hàng  đặt

    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists(): #  dữ  liệu lấy có tồn tại
         order = order_qs[0]
         if order.items.filter(product__pk=pk).exists():
             order_item.quantity += 1
             order_item.save()
             messages.info(request, "thêm thành công sản phẩm vào giỏ ")
             return  redirect("/", pk=pk)
         else:
             order.items.add(order_item)
             messages.info(request,"sản phẩm đã được thêm vào giỏ hàng")
             return redirect("/", pk=pk)
    else:
         ordered_date = timezone.now()
         order = Order.objects.create(user=request.user, ordered_date=ordered_date)
         order.items.add(order_item)
         messages.info(request,"sản phẩm được thêm vào giỏ")
         return redirect("/", pk=pk)

#  thêm  1 số lượng của 1 sản phẩm
def add_item(request,pk):
    product = Product.objects.get(pk=pk)  # lấy theo id
    # đặt hàng
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )
    # lấy dữ liệu từng sản phẩm  mà khách hàng  đặt

    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():  # dữ  liệu lấy có tồn tại
        order = order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            if order_item.quantity < product.product_availabale_count :
                order_item.quantity += 1
                order_item.save()
                return redirect("carts")
            else:
                messages.info(request,"sản phẩm không còn")
                return redirect("carts")
        else:
            order.items.add(order_item)
            messages.info(request, "sản phẩm đã được thêm vào giỏ hàng")
            return redirect("product_details", pk=pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "sản phẩm được thêm vào giỏ")
        return redirect("product_details", pk=pk)

#  xóa đi 1 số lượng của 1 sản phẩm
def remove_item(request,pk):
    item = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False,
    )

    if order_qs.exists():  # dữ  liệu lấy có tồn tại
        order = order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            order_item = OrderItem.objects.filter(
                product=item,
                user=request.user,
                ordered=False,
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()

            else:
                order_item.delete()
            messages.info(request, "sản phẩm không còn")
            return redirect("carts")
        else:

            messages.info(request, "sản phẩm đã không còn trong giỏ hàng")
            return redirect("carts")
    else:
        messages.info(request, "bạn không có đơn đặt hàng nào")
        return redirect("carts")

