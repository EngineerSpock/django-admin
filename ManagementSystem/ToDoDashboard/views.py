from django.http import HttpResponse


# Create your views here.

def index(request):
    print(request)
    return HttpResponse('<h1>Front-End. A stub.</h1>')
