from django.urls import path,include
from User import views

app_name = "webuser"

urlpatterns=[
    path("homepage/",views.homepage,name="homepage"),
    path("myprof/",views.myprofile,name="myprofile"),
    path("editprof/",views.editprofile,name="editprofile"),
    path("changepass/",views.changepass,name="changepassword")
]

