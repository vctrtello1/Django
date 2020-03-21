from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('costumer/<str:pk_test>/', views.costumer, name="costumer"),
    path('create_order/', views.createOrder, name="create_order"),
    path(
        'update_order/<str:pk>/', views.updateOrder,
        name="update_order"),
    path(
        'delete_order/<str:pk>/', views.deleteOrder,
        name="delete_order"),
]
