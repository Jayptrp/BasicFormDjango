from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp.models import myDatabase

# Create your views here.
def index(request):
    db = myDatabase.objects.all()
    return render(request,'index.html',{"db":db})

def about(request):
    return render(request,'about.html')

def form(request):
    if request.method == "POST":
        name = request.POST["name"]
        number = request.POST["number"]
        database = myDatabase.objects.create(name=name,number=number)
        database.save()
        return redirect("/")
    else:
        db = myDatabase.objects.all()
        return render(request,'form.html',{"db":db})
    
def edit(request,myDatabase_id):
    data = myDatabase.objects.get(id=myDatabase_id)
    if request.method == "POST":
        name = request.POST["name"]
        number = request.POST["number"]
        data.name = name
        data.number = number
        data.save()
        return redirect("/")
    else:
        return render(request,'edit.html',{"name":data.name,"number":data.number})
    
def delete(request,myDatabase_id):
    data = myDatabase.objects.get(id=myDatabase_id)
    data.delete()
    return redirect('/')