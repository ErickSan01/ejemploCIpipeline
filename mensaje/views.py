from django.shortcuts import render


# Create your views here.
def hola(request):
    return render(request, 'hola.html')

def hola2(request):
    return render(request,'hola.html')
