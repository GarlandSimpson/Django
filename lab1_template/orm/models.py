from django.db import models


class User(models.Model):
    # CharField for user's first name
    first_name = models.CharField(null=False, max_length=30, default='John')
    # CharField for user's last name
    last_name = models.CharField(null=False, max_length=30, default='Doe')
    # DateField for user's date of birth
    dob = models.DateField(null=True)
