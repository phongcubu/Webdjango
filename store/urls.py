from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('category/<slug:category_slug>/', views.shop, name='products_by_category'),
    path('add_product', views.add_product, name='add_product'),
    path('product_details/<pk>', views.product_details, name='product_details'),
    path('check_out/', views.check_out, name='check_out'),
    path('search/', views.search, name='search'),
    path('submit_review/<int:pk>', views.submit_review, name='submit_review'),
    path('contact/', views.contact, name='contact'),
   
]