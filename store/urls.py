from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.main, name="main"),
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),

]