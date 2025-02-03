from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.userlogin,name='login'),
    path('signup/',views.sign_up,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.userlogout,name='logout'),
    path('change/',views.userpasschange,name='changepass'),
    path('change1/',views.userpasschange1,name='changepass1'),
    path('userdetail/<int:id>',views.userdetail,name="userdetail"),
    path('dashboard/',views.userdashboard, name="dashboard")

]
