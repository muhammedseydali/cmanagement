from django.urls import path  
from . import views


urlpatterns = [    
    path('index/', views.seyd),
    path('show/',views.hello),
    path('delete/<int:id>',views.destroy),
    path('item/',views.ali),
    path('alishow/',views.alishow),
    path('alidelete/<int:id>',views.alidelete),
    path('vendorindex/',views.vendr),
    path('vendorshow/',views.vendrshow),
    path('vendordelete/<int:id>',views.vendrdelete),
    path('location/',views.loc), 
    path('locationshow/',views.locshow),
    path('locationdelete/<int:id>',views.locdelete), 
    path('home/',views.hom),
    path('inventory/',views.inv),
    path('inventshow/',views.invshow),
    path('inventdelete/<int:id>',views.invdelete),
    ]