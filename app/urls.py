from django.urls import path
from app import views

# name="index" mahnje function name exactly index aahe te sangtoy apan.

urlpatterns = [
      path('',views.index,name="index"),
      path('insert',views.insertData,name="insertData"),
      path('update/<id>',views.updateData,name="updateData"),
      path('delete/<id>',views.deleteData,name="deleteData"),
]