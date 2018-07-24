from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('welcome/<user_email>', views.welcome, name='welcome'),
    path('friends/<user_email>', views.friends, name='friends'),
   # path('activity/',views.activity, name='activity'),
    path('<user_email>/', views.detail, name='detail'),
]