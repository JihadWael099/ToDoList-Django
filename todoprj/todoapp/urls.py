from django.urls import path

from . import views

urlpatterns=[

    path('home',views.home,name='home-page'),
    path('register',views.register,name='register-page'),
    path('login',views.login_view,name='login-page'),
    path('',views.login_view,name='login-page'),
    path('delete-task/<str:name>/',views.DeleteTask,name='delete'),
    path('update-task/<str:name>/',views.Update,name='update'),
    path('logout/',views.LogoutView,name='logout'),
]