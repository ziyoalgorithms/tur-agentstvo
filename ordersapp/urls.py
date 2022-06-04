from django.urls import path

import ordersapp.views as ordersapp


app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OderList.as_view(), name='orders_list'),
    path('create/', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    path('read/<int:pk>/', ordersapp.OrderRead.as_view(), name='order_read'),
    path('delete/<int:pk>/', ordersapp.OrderDelete.as_view(), name='order_delete'),
    path('forming/complete/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),
]

