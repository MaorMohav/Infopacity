from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World')

def new_site(request):
    return HttpResponse('New')