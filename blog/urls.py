from django.urls import path
from . import views


urlpatterns = [
       path('',views.post_list,name='post_list'),
       path('view/<int:pk>/', views.post_view, name='post_view'),
       path('new/',views.new_post,name='new_post'),
       path('view/<int:pk>/ediit', views.edit_post,name='edit_post'),
       path('delete/<int:pk>',views.del_post,name='del_post')


    ]