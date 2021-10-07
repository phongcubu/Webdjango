from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect,get_object_or_404

from cart.models import Order
from store.forms import ProductForm,ContactForm
from store.models import *
from django.db.models import Q
from django.http import  HttpResponse
from .forms import ReviewForm


def shop(request, category_slug=None):
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories)
    else:
        products = Product.objects.all().order_by('id')
    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(products, 5)
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'app/shop.html', context=context)
#  thêm sản mới từ trang chử
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request," thêm sản phẩm thành công ")
            return redirect("add_product")
        else:
            messages.info(request,"Chưa có sản phẩm nào được thêm ")
    else:
        form = ProductForm()
    return render(request, 'app/add_product.html', {'form':form})

#  xem sản phẩm chi tiết
def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = ReviewRating.objects.filter(product_id=pk, status=True)
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'app/product_details.html',context=context )

def search(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        products = Product.objects.order_by('-created_date').filter(Q(name__icontains=q) | Q(desc__icontains=q) | Q(category__category_name__icontains=q))
        product_count = products.count()
        context = {
            'products':products,
            'q': q,
            'product_count': product_count
        }
        print(product_count)

        return  render(request, 'app/shop.html',context=context)
@login_required(login_url='user_login') # điều kiện vào giỏ hàng phải đăng nhập
def check_out(request):
    if Order.objects.filter(user=request.user, ordered=False):
        order = Order.objects.get(user=request.user,ordered=False)
        return render(request, 'app/check_out.html',{'order':order})


    return render(request,'app/check_out.html')

def submit_review(request,pk):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating() # liên kết dữ liệu với model form
               #lấy dữ liệu đầu vào
                data.rating = form.cleaned_data['rating']
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = pk
                data.user_id = request.user.id
                data.save() # lưu vào bảng dữ liệu
                messages.success(request, "Cảm ơn bạn! Đánh giá của bạn đã được gửi.")
                return redirect(url)
    return redirect(url)

# contact

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Cảm ơn bạn đã phản hồi cho chúng tôi!")
        else:
            messages.error(request, "Gửi lên chưa thành công" )
    context = {'form':form}
    return render(request, 'app/contact.html',context=context)




