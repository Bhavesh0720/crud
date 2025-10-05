from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name