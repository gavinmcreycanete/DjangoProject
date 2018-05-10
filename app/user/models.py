from django.db import models


class User(models.Model):
    """ User Table """

    # first name with a maximum of 50 characters.
    first_name = models.CharField(max_length=50)

    # last name with a maximum of 50 characters.
    last_name = models.CharField(max_length=50)

    # Gmail or Yahoo email
    email = models.CharField(max_length=30)

    # username with a maximum of 30 characters.
    username = models.CharField(max_length=30)

    # password with a maximum of 30 characters and no restrictions.
    password = models.CharField(max_length=30)

    def __str__(self):
        """ Return username """

        return self.username

# Create your models here.
