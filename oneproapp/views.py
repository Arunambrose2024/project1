from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):
    return  render(request,"onepage.html")

def about(request):
    return render(request,"about.html")