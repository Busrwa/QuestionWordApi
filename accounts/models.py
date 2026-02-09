from django.contrib.auth.models import AbstractUser
from django.db import models

class CrudUser(AbstractUser):
    # Define custom fields here if needed
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('team_lead', 'Team Lead'),
        ('member', 'Member'),
        ('viewer', 'Viewer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')

    # Add related_name to avoid conflicts with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Add a custom related_name here
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Add a custom related_name here
        blank=True
    )
