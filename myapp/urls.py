from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('del_obj/<int:id>/',DeleteData,name='del_obj'),
    path('up_obj/<int:id>/',UpdateData,name='up_obj'),
    path('sub/',sub,name='sub'),
]
