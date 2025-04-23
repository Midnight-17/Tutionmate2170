from django.urls import path
from . import views


app_name = "tutionmate"
urlpatterns =[
    path("", views.admin, name = "admin",),
    path("test", views.test, name = "test"),
    path("profile/<str:tutor_name>", views.profile, name="profile"),
<<<<<<< HEAD
    path("data", views.data, name="data")
=======
    path("Discovernew/", views.discover, name="discover")
>>>>>>> refs/remotes/origin/main

]