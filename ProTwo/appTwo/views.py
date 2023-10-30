from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("<h1>Home Url</h1>")


def colorexperts(request):
    return HttpResponse("<h1>Colorexpertsbd view url</h1>")

# def index(request):
#     my_dict = {'insert_me':"Hello I am from views.py file"}
#     return render(request,'index.html',context=my_dict)

def index(request):
    my_dict = {'insert_me':"Hello I am from subtemplates/index.html file"}
    return render(request,'subtemplates\index.html',context=my_dict)

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html', context=helpdict)
