from django.urls import path
from . import views


app_name = "tutionmate"
urlpatterns =[
    path("", views.homepage, name="homepage"),
    path('newdiscover', views.newdiscover, name='newdiscover'),
    path('loginpage', views.loginpage, name="loginpage"),
    path('login1', views.login1, name="login1"),
    path('profile2/<str:name>',views.profile2, name="profile2"),
    path('my_profile/<str:name>', views.my_profile, name="my_profile"),
    path('edit/', views.edit, name='edit')

]