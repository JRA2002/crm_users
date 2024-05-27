from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path("complaint_list/",views.ComplaintView.as_view(), name='complaint_list'),
    path('complaint/',views.ComplaintFormView, name='complaint'),
    path("clienthome/",views.ClientHome.as_view(), name="clienthome"),
    path('register/',views.RegistrationView.as_view(), name="registration"),
]