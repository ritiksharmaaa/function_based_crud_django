from django.shortcuts import render 
from django.contrib import messages 
from django.http import HttpResponseRedirect
from . forms import UserForm
from . models import User 

# Create your views here.

def Update_data(request , id ):
    instance = User.objects.get(id=id)
    if request.method == "POST":
        fm = UserForm ( request.POST , instance=instance)
        if fm.is_valid():
            fm.save()
            messages.success(request , " Student data update succesfully ")
            return HttpResponseRedirect('/')
    else:
        fm = UserForm(initial={'name' : instance.name , 'email' : instance.email , 'password' : instance.password })
    context ={
        'form' : fm ,
    }
    return render (request , 'enroll/update.html' , context)


def delete_data(request , id ):
    data = User.objects.get(id=id)
    data.delete()
    messages.success(request , "Data is deleted ")
    return HttpResponseRedirect("/")


def addshow_data(request):
    if request.method == "POST":
        fm = UserForm(request.POST )
        if fm.is_valid():
            fm.save()
            messages.success(request , ' Student Add Successfuly ')
        return HttpResponseRedirect("/")
    else:
        fm = UserForm()
    stu = User.objects.all()
    context={
        'form' : fm ,
        'datas' : stu ,
    }
    return render (request, 'enroll/index.html' ,context )
