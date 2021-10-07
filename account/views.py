from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from store.models import Customer
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'yêu cầu đăng nhập lại ')
    return render(request,'accounts/login.html')

def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
        phone = request.POST.get('phone_field')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request," tên người dùng đã tồn tại !")
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request, " email này đã được đăng kí !")
                    return redirect('user_register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    data = Customer(user=user, phone_field=phone)
                    data.save()
                    # đăng nhập
                    curr_user = authenticate(username=username,password=password)
                    if curr_user is not  None:
                        login(request,user)
                        return redirect('/')
        else:
            messages.info(request,'cố lỗi ở đăng kí')
            return redirect('user_register')

    return render(request,'accounts/register.html')
def user_logout(request):
    logout(request)
    return redirect('/')