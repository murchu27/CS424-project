from django.db import models

# Create your models here.
class Production(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date_time   = models.DateTimeField(null=True)
    price       = models.DecimalField(max_digits = 5, decimal_places=2, null=True)

    def __str__(self): #change descriptor of production on homepage
        return self.name
