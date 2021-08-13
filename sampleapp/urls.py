from django.urls import path
from . import views

urlpatterns = [
    path('sample', views.fnSample),
    path('master',views.fnAdminMaster),
    path('home/',views.fnHome),
    path('samplemaster',views.fnMaster),
    path('test',views.fnTest),
    path('app1',views.fnapp1),
    path('crud/',views.fncrud)
    
]