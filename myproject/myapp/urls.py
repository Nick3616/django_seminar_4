from django.urls import path
from . import views
from .views import user_orders

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/<int:name_id>/', views.user_orders, name='user_orders'),
    path('orders_filtered/<int:name_id>/', views.user_orders_filtered, name='user_orders_filtered'),
    path('commodity_form/', views.commodity_form, name='commodity_form'),
    path('edit_commodity/<int:commodity_id>/', views.edit_commodity, name='edit_commodity'),
]
