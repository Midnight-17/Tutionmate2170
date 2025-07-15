from django.urls import path
from . import views


app_name = "tutionmate"
urlpatterns =[
    path("", views.admin, name = "admin",),
    path("test", views.test, name = "test"),
    path("profile/<str:tutor_name>", views.profile, name="profile"),
    path("data", views.data, name="data"),
    path("Discovernew/", views.discover, name="discover"),
    path("homepage",views.homepage, name="homepage"),
    path('newdiscover', views.newdiscover, name='newdiscover'),
    path('loginpage', views.loginpage, name="loginpage"),
    path('signup', views.signup, name="signup"),
    path('create-teacher/', views.create_teacher_view, name="create_teacher"),
    path('login1', views.login1, name="login1"),
    path('profile2/<str:name>',views.profile2, name="profile2"),
    path('my_profile/<str:name>', views.my_profile, name="my_profile")

]