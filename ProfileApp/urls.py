from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('Profile/', views.Profile, name="Profile"),
    path('Education/', views.Education, name="Education"),
    path('Attention/', views.Attention, name="Attention"),
    path('Career/', views.Career, name="Career"),
    path('Product/', views.Product, name="Product"),
    path('RoleModel/', views.RoleModel, name="RoleModel"),
    path('ShowData/', views.ShowData, name='ShowData')
]