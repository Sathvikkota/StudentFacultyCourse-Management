from django.db.models import Q
from django.shortcuts import render,redirect

from .models import Admin, Student, Course, Faculty
from .forms import AddFacultyForm, AddStudentForm


# Create your views here.
def adminhome(request):
    return render(request,"adminhome.html")

def logout(request):
    return render(request,"login.html")

def checkadminlogin(request):
    adminuname=request.POST["uname"]
    adminpwd=request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)

    if flag:
        request.session["auname"]=adminuname
        return render(request,"adminhome.html",{"adminuname":adminuname})
    else:
        #return HttpResponse("Login Failed")
        msg="Login Failed"
        return render(request,"login.html",{"message":msg})

def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]

    flag = Student.objects.filter(Q(studentid=sid) & Q(password=pwd))
    print(flag)

    if flag:
        request.session["sid"] = sid
        return render(request, "studenthome.html", {"sid": sid})
    else:
        # return HttpResponse("Login Failed")
        msg = "Login Failed"
        return render(request, "studentlogin.html", {"message": msg})

def viewstudents(request):
    auname = request.session["auname"]
    students=Student.objects.all()
    count=Student.objects.count()
    return render(request,"viewstudents.html",{"studentdata":students,"count":count,"adminuname":auname})

def viewcourses(request):
    auname = request.session["auname"]
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursedata":courses,"count":count,"adminuname":auname})

def viewfaculty(request):
    auname = request.session["auname"]
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})

def admincourse(request):
    auname = request.session["auname"]
    return render(request,"admincourse.html",{"adminuname":auname})

def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})

def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname} )

def addcourse(request):
    auname = request.session["auname"]
    return render(request,"addcourse.html",{"adminuname":auname})

def insertcourse(request):
    auname = request.session["auname"]
    if request.method=="POST":
        dept= request.POST["dept"]
        prog= request.POST["program"]
        ay= request.POST["ay"]
        sem= request.POST["sem"]
        year= request.POST["year"]
        ccode= request.POST["ccode"]
        ctitle= request.POST["ctitle"]

        course=Course(department=dept,program=prog,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle)
        Course.save(course)

        msg="Course Added Successfully"

        return render(request,"addcourse.html",{"message":msg,"adminuname":auname})

def deletecourse(request):
    auname = request.session["auname"]
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"deletecourse.html",{"coursedata":courses,"count":count,"adminuname":auname})

def coursedeletion(request,cid):

    Course.objects.filter(id=cid).delete()
    return redirect(deletecourse)   #deletecourse is a url name not based on html page name
    #return HttpResponse("Course Deleted Successfully")

def addfaculty(request):
    auname = request.session["auname"]
    form = AddFacultyForm()  # non parameterized constructor
    if request.method=="POST":
        form1=AddFacultyForm(request.POST)# parameterized constructor
        if form1.is_valid():
            form1.save()  # saves data to faculty_table
            message="Faculty Added Successfully"
            return render(request,"addfaculty.html",{"msg":message,"form":form,"adminuname":auname})
        else:
            message = "Failed to Add Faculty"
            return render(request, "addfaculty.html", {"msg": message, "form": form,"adminuname":auname})
    return render(request,"addfaculty.html",{"form":form,"adminuname":auname})

def deletefaculty(request):
    auname = request.session["auname"]
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"deletefaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})

def facultydeletion(request,fid):

    Faculty.objects.filter(id=fid).delete()
    return redirect(deletefaculty)   #deletefaculty is a url name not based on html page name
    #return HttpResponse("Course Deleted Successfully")

def addstudent(request):
    auname = request.session["auname"]
    form = AddStudentForm()  # non parameterized constructor
    if request.method=="POST":
        form1=AddStudentForm(request.POST)# parameterized constructor
        if form1.is_valid():
            form1.save()  # saves data to faculty_table
            message="Student Added Successfully"
            return render(request,"addstudent.html",{"msg":message,"form":form,"adminuname":auname})
        else:
            message = "Failed to Add Student"
            return render(request, "addstudent.html", {"msg": message, "form": form,"adminuname":auname})
    return render(request,"addstudent.html",{"form":form,"adminuname":auname})

def deletestudent(request):
    auname = request.session["auname"]
    student=Student.objects.all()
    count = Student.objects.count()
    return render(request,"deletestudent.html",{"studentdata":student,"count":count,"adminuname":auname})

def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    return redirect(deletestudent)   #deletefaculty is a url name not based on html page name
    #return HttpResponse("Course Deleted Successfully")

def facultycoursemapping(request):
    auname = request.session["auname"]
    return render(request,"facultycoursemapping.html",{"adminuname":auname})

def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})

