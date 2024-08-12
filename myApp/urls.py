from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('form',views.form),
    path('edit/<myDatabase_id>',views.edit),
    path('delete/<myDatabase_id>',views.delete)
]