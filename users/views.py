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
from django.http import HttpResponse
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# Create your views here.

def create_pdf(request):
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

def set_cookie_view(request):
    response = HttpResponse("La cookie ha sido establecida")
    # Establece una cookie
    response.set_cookie('mi_cookie', 'valor_cookie', max_age=3600)  # La cookie expira en 1 hora
    return response

def get_cookie_view(request):
    valor_cookie = request.COOKIES.get('mi_cookie')
    if valor_cookie:
        return HttpResponse(f'El valor de la cookie es: {valor_cookie}')
    else:
        return HttpResponse('No se encontró la cookie')

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
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            id_complaint = complaint.id
            messages.success(request, f'¡Complaint N° {id_complaint} sent successfully!')
            return render(request, 'users/client_home.html')
    else:
        form = ComplaintForm()
    return render(request, 'users/complaint_form.html', {'form': form})

class ClientHome(LoginRequiredMixin, TemplateView):
    template_name = "users/client_home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        context['num_visits'] = num_visits
        return context

class RegistrationView(View):
    
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
    


