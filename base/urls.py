from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('upload/',views.upload,name='upload'),
    path('logout',views.logoutUser,name='logout'),
]