from django.contrib import admin
from store.models import *


# người dùng
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_field')


#  sản phẩm
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'product_availabale_count', 'category', 'created_date',  'is_available')
    list_filter = ('category', 'price')
#  đánh giá
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('user','subject', 'review', 'rating','created_at' ,'status')
    list_filter = ('created_at','status','user')

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Category)
admin.site.register(ReviewRating,ReviewRatingAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)