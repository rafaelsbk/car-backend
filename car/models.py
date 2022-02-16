from django.db import models

# Create your models here.
class Car(models.Model):
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    tipo_car = models.CharField(max_length=60)
    cor = models.CharField(max_length=60)
    ano = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
