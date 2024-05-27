from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path("clients/",views.ClientView.as_view(), name='client'),
    path('complaint/',views.ComplaintFormView, name='complaint'),
]