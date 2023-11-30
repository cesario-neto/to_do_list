from django.urls import path
from . import views

urlpatterns = [
    # index
    path('', views.index, name='index'),

    # account
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    # task
    path('home/', views.home, name='home'),

]
