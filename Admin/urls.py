from django.urls import path
from Admin import views
#key value
app_name="webadmin"
urlpatterns = [
    path('dis/',views.district,name='districtrefresh'),
    #delete query syntax
    path('deldis/<int:did>',views.deletedis,name="deleted"),
    path('cat/',views.category),
    path('place/',views.place),
    path('sub/',views.sub), 
    path('reg/',views.adreg),
    path('editdis/<int:did>',views.editdis,name="edited")
]
