from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('home/', views.home, name='home'),
    path('p_home/', views.p_home, name='p_home'),
    path('d_register', views.d_register, name='d_register'),
    path('p_register', views.p_register, name='p_register'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('signin/', views.signin, name='signin'),
    path('p_signin/', views.p_signin, name='p_signin'),
    path('d_profile/', views.d_profile, name='d_profile'),



]
