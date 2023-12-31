from django.urls import path
from . import views

urlpatterns = [

    # account
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    # task CRUD
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit_task/<slug:slug>/', views.edit_task, name='edit_task'),
    path('delete_task/<task_id>/', views.delete_task, name='delete_task'),

]
