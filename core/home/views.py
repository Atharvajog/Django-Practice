from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples=[
        {'name':'jon','age':24},
        {'name':'dave','age':17},
        {'name':'rohan','age':28},
        {'name':'rahul','age':26},
    ]
    return render(request,"index.html",context={'peoples':peoples,'page':'home'})

def about(request):
    context={'page':'about'}
    return render(request,"about.html",context)
def success_page(request):
    return HttpResponse("This is a successpage")
