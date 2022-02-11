from django.urls import path
from . import views


urlpatterns = [
       path('',views.post_list,name='post_list'),
       path('view/<int:pk>/', views.post_view, name='post_view'),


    ]