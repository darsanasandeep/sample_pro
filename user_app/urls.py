from django.urls import path

from . import views

urlpatterns = [
        path('register',views.User_Registration),
        path('',views.user_signup),
        path('login',views.user_login),
        path('logout',views.user_logout),
        path('upload',views.Upload_Images)
]