from django.db import models
from app.user.models import User


class Profile(models.Model):
    """Profile table"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # biography with a maximum of 100 characters.
    bio = models.CharField(max_length=1000)

    # use avatar as label for now.
    avatar = models.CharField(max_length=100)

    def __str__(self):
        """Return avatar"""

        return self.avatar
