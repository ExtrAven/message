from django.shortcuts import get_object_or_404, render

from .models import Services

# Create your views here.


def index(request):
    services = Services.objects.all()
    return render(request, "index.html", {"services": services})


def service_detail(request, id):
    service = Services.objects.get(id=id)
    return render(request, "service_detail.html", {"service": service})
