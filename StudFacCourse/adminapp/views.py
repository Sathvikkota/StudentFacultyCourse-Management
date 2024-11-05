from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin, Student, Course, Faculty, FacultyCourseMapping
from .forms import AddFacultyForm, AddStudentForm, StudentForm
from .decorators import login_required


def login(request):
    if request.method == "POST":
        return checkadminlogin(request)
    return render(request, "login.html")

# Create your views here.
@login_required
def adminhome(request):
    auname = request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})
def logout(request):
    request.session.flush()  # This will clear all session data
    return redirect('login')  # Redirect to the login page after logging out


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


@login_required
def viewstudents(request):
    auname = request.session["auname"]
    students=Student.objects.all()
    count=Student.objects.count()
    return render(request,"viewstudents.html",{"studentdata":students,"count":count,"adminuname":auname})

@login_required
def viewcourses(request):
    auname = request.session["auname"]
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursedata":courses,"count":count,"adminuname":auname})
@login_required

def viewfaculty(request):
    auname = request.session["auname"]
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})

@login_required
def admincourse(request):
    auname = request.session["auname"]
    return render(request,"admincourse.html",{"adminuname":auname})

@login_required
def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})

@login_required
def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname} )
@login_required
def addcourse(request):
    auname = request.session["auname"]
    return render(request,"addcourse.html",{"adminuname":auname})

def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "updatecourse.html", {"adminuname": auname,"courses":courses,"count":count})

def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid ,"adminuname": auname})


def courseupdated(request):
    auname = request.session["auname"]
    cid=request.POST["cid"]
    courseid=int(cid)
    ctitle = request.POST["ctitle"]
    ltps = request.POST["ltps"]
    credits = request.POST["credits"]
    Course.objects.filter(id=courseid).update(coursetitle=ctitle,ltps=ltps,credits=credits)
    msg="Course Updated Successfully"
    return render(request,"courseupdation.html",{"msg":msg,"adminuname":auname,"cid":cid})
@login_required
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
        ltps=request.POST["ltps"]
        credits=request.POST["credits"]

        course=Course(department=dept,program=prog,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)
        Course.save(course)

        msg="Course Added Successfully"

        return render(request,"addcourse.html",{"message":msg,"adminuname":auname})


@login_required
def deletecourse(request):
    auname = request.session["auname"]
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"deletecourse.html",{"coursedata":courses,"count":count,"adminuname":auname})
@login_required
def coursedeletion(request,cid):

    Course.objects.filter(id=cid).delete()
    return redirect(deletecourse)   #deletecourse is a url name not based on html page name
    #return HttpResponse("Course Deleted Successfully")
@login_required
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
@login_required
def deletefaculty(request):
    auname = request.session["auname"]
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"deletefaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})
@login_required
def facultydeletion(request,fid):

    Faculty.objects.filter(id=fid).delete()
    return redirect(deletefaculty)   #deletefaculty is a url name not based on html page name
    #return HttpResponse("Course Deleted Successfully")
@login_required
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

def updatestudent(request):
    auname = request.session["auname"]
    student=Student.objects.all()
    count = Student.objects.count()
    return render(request,"updatestudent.html",{"studentdata":student,"count":count,"adminuname":auname})


@login_required
def deletestudent(request):
    auname = request.session["auname"]
    student=Student.objects.all()
    count = Student.objects.count()
    return render(request,"deletestudent.html",{"studentdata":student,"count":count,"adminuname":auname})
@login_required
def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    return redirect(deletestudent)   #deletefaculty is a url name not based on html page name
    #return HttpResponse("Course Deleted Successfully")

def studentupdation(request,sid):
    auname = request.session["auname"]
    student=get_object_or_404(Student,pk=sid)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            message="Updated Successfully"
            return render(request, "studentupdated.html", {"form": form, "adminuname": auname, "msg": message})
        else:
            message="Updation Failed"
            return render(request, "studentupdated.html", {"form": form, "adminuname": auname, "msg": message})
    else:
        form=StudentForm(instance=student)
    return render(request,"studentupdated.html",{"form":form,"adminuname":auname})
@login_required
def facultycoursemapping(request):
    fmcourses=FacultyCourseMapping.objects.all()
    auname = request.session["auname"]
    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fmcourses})
@login_required
def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})

@login_required
def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("Old Pwd is Correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        msg="Password Updated Successfully"
    else:
        print("Old Password is Incorrect")
        msg="Old Password is Incorrect"
    return render(request,"adminchangepwd.html",{"adminuname":auname,"message":msg})

