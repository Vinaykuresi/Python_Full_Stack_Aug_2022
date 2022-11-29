from django.shortcuts import render 
from django.http import HttpResponse

def homePage(request):
    return HttpResponse(request, 'home.html')

def view_profile(request):
    pass 

def edit_profile(request):
    pass 

def delete_profile(request):
    pass 