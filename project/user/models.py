from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.email
