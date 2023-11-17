from django import views
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    
    path('addstudent',views.addstudent,name='addstudent'),
    path('addcourse1',views.addcourse1,name='addcourse1'),
    path('addstudent1',views.addstudent1,name='addstudent1'),
    
    path('showstudent',views.showstudent,name='showstudent'),

    path('editstudent/<int:pk>',views.editstudent,name='editstudent'),
    path('editstudent1/<int:pk>',views.editstudent1,name='editstudent1'),

    path('deletestudent/<int:pk>',views.deletestudent,name='deletestudent'),


]
