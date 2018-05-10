from django.db import models
from profiles.models import Profile


class Tags(models.Model):
    """ Tag table """

    profile = models.ManyToManyField(Profile)

    # Tag name
    name = models.CharField(max_length=50)

    def __str__(self):
        """ Return tag name """

        return self.name

# Create your models here.
