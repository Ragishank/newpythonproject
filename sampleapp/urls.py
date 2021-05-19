from django.urls import path
from . import views

urlpatterns = [
    path('sample', views.fnSample),
    path('test',views.fnTest),
    path('web',views.fnWeb)
]