from django.contrib import admin
from app.user.models import User
from profiles.models import Profile
from app.tag.models import Tags

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Tags)

# Register your models here.
