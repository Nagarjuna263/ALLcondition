from django.shortcuts import render

# Create your views here.
def if_1(request):
    d=context={'a':50,'b':30}
    return render(request,'if_1.html',d)

def ifandelse(request):
    d=context={'a':500,'b':800}
    return render(request,'ifandelse.html',d)