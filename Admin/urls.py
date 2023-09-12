from django.urls import path
from Admin import views
urlpatterns = [
    path('dis/',views.district),
    path('cat/',views.category),
    path('place/',views.place),
    path('sub/',views.sub),
]
