from django.db import models

class Auto(models.Model):

    modelo = models.CharField(max_length=30)

    marca = models.CharField(max_length=30)   

    def __str__(self):
        return f'Auto({self.id}): {self.marca} - {self.modelo}'

