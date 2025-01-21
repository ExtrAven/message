from django.urls import path
from .views import index, service_detail

app_name = "main_app"

urlpatterns = [
    path("", index, name="index"),
    path("<int:id>/", service_detail, name="service_detail"),
]
