from django.urls import path
from . import views

urlpatterns = [
    path('carts/', views.carts, name='carts'),
    path('add_to_cart/<pk>', views.add_cart, name='add_cart'),
    path('add_item/<int:pk>', views.add_item, name='add_item'),

    path('remove_item/<int:pk>', views.remove_item, name='remove_item'),

]