from django.db import models
from store.models import Product
from django.contrib.auth.models import User
from store.models import Customer

# SẢN PHẨM TRONG GIỎ hàng
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)  # đã đặt hàng
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self): # tổng tiền trong mỗi sản phẩm
        return self.quantity * self.product.price


    def get_final_price(self): #giá  tổng cần thanh toán trong tất cả sản phẩm
        return self.get_total_item_price()

# giỏ hàng
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField() #ngày đặt hàng
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def get_total_count(self):
        order = Order.objects.get(pk=self.pk)
        return order.items.count()



