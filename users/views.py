from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Client
from .forms import ComplaintForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "users/home.html"

class ClientView(ListView):
    model = Client
    template_name = "users/client.html"
    context_object_name = "clients"

def ComplaintFormView(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/home.html')
    else:
        form = ComplaintForm()
    return render(request, 'users/complaint_form.html', {'form': form})

