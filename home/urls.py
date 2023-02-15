from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path('newcostmer',views.newcostmer, name="newcostmer"),
    path('weekplan', views.weekplan, name='last_7_days_data'),
    path('dayplan',views.dayplan, name="dayplan"),
    path('new_customers/<str:date>/', views.new_customers_on_date, name='new_customers_on_date'),
    path('retrieve_data/', views.retrieve_data, name='retrieve_data'),
    path('dowonload_newco/', views.dowonload_newco, name='dowonload_newco'),
    path('dowonload_dayreport/', views.dowonload_dayreport, name='dowonload_dayreport'),
    path('dowonload_weekRepo/', views.dowonload_weekRepo, name='dowonload_weekRepo'),
    ]
