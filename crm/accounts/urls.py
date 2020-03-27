from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('home/', views.home, name="home"),
    path('user/', views.userPage, name="user"),
    path('products/', views.products, name="products"),
    path('costumer/<str:pk_test>/', views.costumer, name="costumer"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path(
        'update_order/<str:pk>/', views.updateOrder,
        name="update_order"),
    path(
        'delete_order/<str:pk>/', views.deleteOrder,
        name="delete_order"),
]
