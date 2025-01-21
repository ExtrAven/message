from django.db import models

# Create your models here.


class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    service_image = models.ImageField(upload_to="service_images/")
    service_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name
