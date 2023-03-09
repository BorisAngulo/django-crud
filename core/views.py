from django.shortcuts import render#con render rendferizamos una plantilla

# Create your views here.
def index(request):
    return render(request, 'home.html')