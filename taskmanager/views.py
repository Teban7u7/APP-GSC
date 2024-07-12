from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Asume que tienes un template llamado 'home.html'
