from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.
def thanksmgs(request):
    return render (request,'enroll/regsuccess.html')


def showformsdata(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Valideted')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('Name: ',name)
            print('Email: ',email)
            print('Password:', password)
            return HttpResponseRedirect ('/student/success/')
    else:
        fm = StudentRegistration()  
    return render (request,'enroll/registrationsform.html', {'form':fm})

