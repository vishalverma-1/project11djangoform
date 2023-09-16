from django.shortcuts import render,redirect
from django .http import HttpResponse
from . forms import studentform
from . models import student
def fun(request):
    if request.method=='POST':
        form=studentform(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('read')
    else:
        form=studentform()
        return render(request,'create.html',{'form':form})    
    



def read(request):
    data=student.objects.all()
    return render(request,'read.html',{'data':data})



def delete(request,id):
    obj=student.objects.get(id=id)
    obj.delete()
    return redirect('read')



def edit(request,id):
    data=student.objects.get(id=id)
    if request.method=='POST':
        fm=studentform(request.POST,instance=data)
        if fm.is_valid:
            fm.save()
            return redirect('read')
    else:
        fm=studentform(instance=data)
        return render(request,'edit.html',{'fm':fm})


