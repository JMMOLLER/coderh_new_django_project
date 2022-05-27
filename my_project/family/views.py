from django.shortcuts import render
from family.models import Family
from datetime import datetime

# Create your views here.

def mienbros(request):
    miembro_familia = Family.objects.all()

    fecha_actual = datetime.now()

    context = {
        "miembro_familia": miembro_familia, 
        "fecha_actual" : fecha_actual
        }
    return render(request, "template_1.html", context)

