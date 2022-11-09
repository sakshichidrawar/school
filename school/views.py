from django.shortcuts import render
from school import models
from .forms import firstform,secondform,thirdform,fourthform
from .models import firstclass,secondclass,thirdclass,fourthclass

# Create your views here.
def firstdata(request):
    form=firstform()
    if request.method == 'POST' :
        fm=firstform(request.POST)
        if fm.is_valid():
            sn=fm.cleaned_data['stuname']
            ss=fm.cleaned_data['stusurname']
            sa=fm.cleaned_data['stuage']
            sr=fm.cleaned_data['sturoll_no']
            reg= firstclass(stuname=sn,stusurname=ss,stuage=sa,sturoll_no=sr)
            reg.save()
            fm=firstform()
        else:
            fm=firstform()
    return render(request,'school/first.html',{'form':form})
    
def seconddata(request):
    form=secondform()
    if request.method == 'POST' :
        fm=secondform(request.POST)
        if fm.is_valid():
            sn=fm.cleaned_data['stuname']
            ss=fm.cleaned_data['stusurname']
            sa=fm.cleaned_data['stuage']
            sr=fm.cleaned_data['sturoll_no']
            reg= secondclass(stuname=sn,stusurname=ss,stuage=sa,sturoll_no=sr)
            reg.save()
            fm=secondform()
        else:
            fm=secondform()   
    return render(request,'school/second.html',{'form':form})

def thirddata(request):
    form=thirdform()
    if request.method == 'POST' :
        fm=thirdform(request.POST)
        if fm.is_valid():
            sn=fm.cleaned_data['stuname']
            ss=fm.cleaned_data['stusurname']
            sa=fm.cleaned_data['stuage']
            sr=fm.cleaned_data['sturoll_no']
            reg= thirdclass(stuname=sn,stusurname=ss,stuage=sa,sturoll_no=sr)
            reg.save()
            fm=thirdform()
        else:
            fm=thirdform() 
    return render(request,'school/third.html',{'form':form})  

def fourthdata(request):
    form=fourthform()
    if request.method == 'POST' :
        fm=fourthform(request.POST)
        if fm.is_valid():
            sn=fm.cleaned_data['stuname']
            ss=fm.cleaned_data['stusurname']
            sa=fm.cleaned_data['stuage']
            sr=fm.cleaned_data['sturoll_no']
            reg= fourthclass(stuname=sn,stusurname=ss,stuage=sa,sturoll_no=sr)
            reg.save()
            fm=fourthform()
        else:
            fm=fourthform()
  
    
    return render(request,'school/fourth.html',{'form':form})
