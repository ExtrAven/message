from django.shortcuts import render

# Create your views here.


def index(request):
    message = request.POST.get("username")
    return render(request, "index.html", {"message": message})
