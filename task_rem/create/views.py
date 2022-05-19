from django.shortcuts import render

# Create your views here.

def create_action(request):
    return render(request , 'create.html')
    