from django.db import models

class Department(models.Model):

    department_name = models.CharField(max_length=100)
    budget = models.CharField(max_length=20)