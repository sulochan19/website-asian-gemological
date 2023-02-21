from django.shortcuts import render
from .models import Stone
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def verification(request):
    if request.method == 'POST':
        verification_number = request.POST['verification_number']
        if Stone.objects.filter(verification_number=verification_number).exists():
            context = {
                'stone_details': Stone.objects.filter(verification_number=verification_number),
            }
            return render(request,'verification.html',context=context)
        else:
            return render(request, 'verification.html')