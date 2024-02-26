from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, World. You're at the Certificate Expiry Reminder Index")