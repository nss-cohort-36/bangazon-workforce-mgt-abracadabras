from django.db import models

class Department(models.Model):

    department_name = models.CharField(max_length=100, null=True, blank=True)
    budget = models.CharField(max_length=20, null=True, blank=True)