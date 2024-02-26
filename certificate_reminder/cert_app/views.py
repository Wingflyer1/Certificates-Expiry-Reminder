from django.shortcuts import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, World. You're at the Certificate Expiry Reminder Index")