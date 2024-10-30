from django.db import models
from django.contrib.auth.models import User
from typing import TYPE_CHECKING

# Institute Type
class InstituteType(models.TextChoices):
    SCHOOL = 'SCHOOL', 'School'
    COLLEGE = 'COLLEGE', 'College'
    COACHING = 'COACHING', 'Coaching'

# Institue model 
class Institute(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # `type` field defined as CharField but using InstituteType for choices
    type: 'InstituteType' = models.CharField(
        max_length=10,
        choices=InstituteType.choices,
        default=InstituteType.SCHOOL
    )
    
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)