
# DJANGO-ADMIN : USERNAME=admin & PASSWORD = admin.
from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    data=Student.objects.all() # Student.objects.all() matlab student table se all data fetch karenge. just like sql query:- select * from student 
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        # query ko save karna menas upper ke sare fields ke data ko database main add kar rah hain.
        # name=name yaha hum naya variable jiska same name hain us main name ka data dal rahae hain.
        query = Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"data Inserted Successfully")
        return redirect("/")
    return render(request,"index.html")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender 
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

# context kyoun banate hain taki html page ke sath use bhejne ke liye. j

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Succeefully")
    return redirect("/")
     
    return render(request,"delete.html")

