from django.urls import path
from Guest import views
app_name='webguest'

urlpatterns = [
    path('userreg/',views.userreg,name="userreg"),
    path('ajaxplace',views.ajaxplace,name="ajaxplace"),
    path('login/',views.login,name="login"),

]