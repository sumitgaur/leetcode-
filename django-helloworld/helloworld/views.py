from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def users(request):
    return HttpResponse("Users")
