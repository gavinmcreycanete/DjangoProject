from django.shortcuts import render
from app.user.models import User
from django.http import HttpResponse


def profile(request):
    if 'username' in request.GET:
        for user in User.objects.all():
            if user.username == request.GET['username']:
                return render(request, 'profile.html')
        return HttpResponse('Not yet registered')
    else:
        return HttpResponse('Invalid query string')
# Create your views here.
