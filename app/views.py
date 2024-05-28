from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

def insert_Student(request):
    ETO = StudentForm()
    d = {'ETO': ETO}
    if request.method == 'POST':
        TFD = StudentForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Student data inserted')
        else:
            return HttpResponse('Invalid data')
    return render(request, 'insert_student.html', d)



def insert_Guardian(request):
    EGO=GuradianForm()
    d={'EGO':EGO}
    if request.method=='POST':
        TFD=GuradianForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('gurdian data inserted')
        else:
            return HttpResponse('invalid data')
    return render (request,'insert_guardian.html',d)