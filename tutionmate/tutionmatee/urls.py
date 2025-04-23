from django.urls import path
from . import views


app_name = "tutionmate"
urlpatterns =[
    path("", views.admin, name = "admin",),
    path("test", views.test, name = "test"),
    path("profile/<str:tutor_name>", views.profile, name="profile"),
    path("data", views.data, name="data")

]