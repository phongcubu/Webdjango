from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    phone_field = models.CharField(max_length=13, blank=False )

    def __str__(self):
        return self.user.username

# phân loại hạng mục :
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

# chi tiết sản phẩm :
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    product_availabale_count = models.IntegerField(default=0)
    img = models.ImageField(upload_to='product/')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)


    # phương thức lấy đường dẫn để thêm 1 sản phẩm vào giỏ hàng khóa chính
    def get_add_to_cart_url(selfs):
        return reverse("store:add-to-cart", kwargs={
            "pk": selfs.pk
        })
    def __str__(self):
        return self.name

#  đánh giá sản phẩm :

class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

#  phần form liên hệ :
class Contact(models.Model):
    name_contact = models.CharField(max_length=100, blank=True)
    email_contact = models.TextField(max_length=100, blank=True)
    phone_contact = models.CharField(max_length=15, blank=True)
    comment_contact = models.TextField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_contact