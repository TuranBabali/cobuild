from django.shortcuts import render
from works.models import Category, Project

def test1(request):
    return render(request,'test1.html')

def index(request):
    context={
        'categories': Category.objects.all(),
        'projects' : Project.objects.all(),
    }
    return render(request,'landing-1.html',context)
    