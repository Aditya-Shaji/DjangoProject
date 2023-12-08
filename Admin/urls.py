from django.urls import path
from Admin import views
#key value
app_name="webadmin"
urlpatterns = [
    path('dis/',views.district,name='districtrefresh'),
    path('cat/',views.category,name='catrefresh'),
    #delete query syntax
    path('deldis/<int:did>',views.deletedis,name="deleted"),
    path('cat/',views.category),
    path('place/',views.place,name='plarefresh'),
    path('sub/',views.subcategory,name='subrefresh'), 
    path('reg/',views.adreg),
    path('editdis/<int:did>',views.editdis,name="editdis"),
    path('editcat/<int:did>',views.editcat,name="editcat"),
    path('delplace/<int:did>',views.delplace,name="delpla"),
    path('delsub/<int:did>',views.delsub,name="delsub"),
     path('brand/',views.brand,name='brandrefresh'),
]
