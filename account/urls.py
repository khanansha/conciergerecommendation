from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('cuisine/', views.cuisine, name='cuisine'),
    path('sport/', views.sport, name='sport'),
    path('travel/', views.travel, name='travel'),
    path('event/', views.event, name='event'),
    path('index/', views.index, name='index'),
    path('recomd/', views.recomd, name='recomd'),

]
