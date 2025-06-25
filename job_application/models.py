from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contact(models.Model):
    """Contact form model"""

    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    message = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} message is: {self.message}"
