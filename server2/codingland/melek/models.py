from django.db import models

# Create your models here.
class Review(models.Model):
    employee_name = models.CharField(max_length=200)
    work_howers = models.IntegerField()
    did_he_comming_late =models.BooleanField()
    descriptions =models.TextField()
