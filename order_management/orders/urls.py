from django.urls import path
from . import views

urlpatterns = [
    # URL to list all orders, handled by the get_orders view
    path('orders/', views.get_orders, name='get_orders'),
    
    # URL to add a new order, handled by the add_order view
    path('orders/add/', views.add_order, name='add_order'),
]
