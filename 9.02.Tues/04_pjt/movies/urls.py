from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
   path('index/', views.index, name = 'index'),
   path('new/', views.new, name = 'new'),
   path('create/', views.create, name='create'),
   path('detail/<int:pk>/', views.detail, name= 'detail'),
   path('edit/<int:pk>/', views.edit, name= 'edit'),
   path('update/<int:pk>/', views.update, name='update'),
   path('delete/<int:pk>/', views.delete, name ='delete'),
   
    
]
