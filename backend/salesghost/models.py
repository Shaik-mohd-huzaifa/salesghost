from django.db import models

# Create your models here.

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    target_audience = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    objective = models.TextField()

    def __str__(self):
        return self.name
