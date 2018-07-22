from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('activity/',views.activity, name='activity'),
    path('<email:user_email>/', views.detail, name='detail'),
]