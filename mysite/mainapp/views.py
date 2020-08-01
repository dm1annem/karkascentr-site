from django.shortcuts import render



def home(request):
    return render(request, 'mainapp/home.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')
