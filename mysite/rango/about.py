from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says here is the about page.</br> <a href='/rango/'>Index</a>")