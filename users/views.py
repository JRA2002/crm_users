from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView, View
from .models import Client
from .forms import ComplaintForm, RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class HomeView(TemplateView):
    template_name = "users/home.html"

class ComplaintView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "users/complaint_list.html"
    context_object_name = "complaints"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['complaints'] = Client.objects.filter(user=context['user'])
        return context
@login_required
def ComplaintFormView(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Complaint enviado con éxito!')
            return render(request, 'users/client_home.html')
    else:
        form = ComplaintForm()
    return render(request, 'users/complaint_form.html', {'form': form})

class ClientHome(LoginRequiredMixin, TemplateView):
    template_name = "users/client_home.html"

class RegistrationView(SuccessMessageMixin, View):
    success_message = 'hollaaa'
    def get(self, request):
        data = {
            'form': RegistrationForm()
        }
        return render(request, "registration/registration.html", data)
    def post(self, request):
        user_create_form = RegistrationForm(request.POST)

        if user_create_form.is_valid():
            user_create_form.save()
            user = authenticate(username=user_create_form.cleaned_data["username"], password=user_create_form.cleaned_data["password1"])
            login(request, user)

            return redirect('clienthome')
        data = {
            'form' : user_create_form
        }
        return render(request, "registration/registration.html", data)

