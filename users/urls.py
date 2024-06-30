from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path("claim_list/",views.ClaimView.as_view(), name='claim_list'),
    path('claim/',views.ClaimFormView, name='claim'),
    path("clienthome/",views.ClientHome.as_view(), name="clienthome"),
    path('register/',views.RegistrationView.as_view(), name="registration"),
    path('set_cookie/',views.set_cookie_view, name='set_cookie'),
    path('get_cookie/', views.get_cookie_view, name='get_cookie'),
    path('pdf/',views.create_pdf, name='pdf'),
]