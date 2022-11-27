from django.shortcuts import render

# Create your views here.
def ifelif1(request):
    d=context={'a':800,'b':990,'c':1000}
    return render(request,'ifelif1.html',d)

def nestedif(request):
    d=context={'a':800,'b':990,'c':100}
    return render(request,'nestedif.html',d)