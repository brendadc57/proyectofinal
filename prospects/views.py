from django.shortcuts import render, get_object_or_404, redirect
from .models import Prospect
from .forms import ProspectForm, SeguimientoForm

def lista_prospects(request):
    prospects = Prospect.objects.all()
    return render(request, 'prospects/lista.html', {'prospects': prospects})

def crear_prospect(request):
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ProspectForm()
    return render(request, 'prospects/form_prospect.html', {'form': form})
