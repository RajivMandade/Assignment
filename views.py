from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

from django.shortcuts import render
slist=[]
# Create your views here.
def home(request):
    return render(request,"home.html")
def info(request):
    if request.method=="POST":
        FirstName=request.POST.get("FirstName")
        Lastname=request.POST.get("LastName")
        email=request.POST.get("email")
        age=request.POST.get("age")
        dob=request.POST.get("DOB")
        Mn=request.POST.get("Mobile")
        t=(FirstName,Lastname,email,age,dob,Mn)
        slist.append(t)
        print(slist)
        return render(request,"home.html")
    else:
        return render(request,"data.html")


def student_list(request):
    
    d={'sl':slist}
    print(d)
    return render(request,"studentList.html",d)
def student_delete(request):
   
    FirstName=request.GET.get("FirstName")
    for i in slist:
        if i[0]==FirstName:
            slist.remove(i)
    
    return render(request,"home.html")