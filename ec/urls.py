from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('product',views.product,name='product'),
    path('addcart',views.addcart,name='addcart'),
    path('user',views.user,name='user'),
    path('view_cart',views.view_cart,name='view_cart'),
    path('remove',views.remove,name='remove'),
    path('placeorder',views.placeorder,name='placeorder'),
]