from adminapp.models import Faculty,FacultyCourseMapping
from django.db.models import Q
from django.shortcuts import render




# Create your views here.

def facultyhome(request):
    fid=request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})

def checkfacultylogin(request):
    fid = request.POST["fid"]
    pwd = request.POST["pwd"]

    flag = Faculty.objects.filter(Q(facultyid=fid) & Q(password=pwd))
    print(flag)

    if flag:
        request.session["fid"] = fid
        return render(request, "facultyhome.html", {"fid": fid})
    else:
        # return HttpResponse("Login Failed")
        msg = "Login Failed"
        return render(request, "facultylogin.html", {"message": msg})

def facultycourses(request):
    fid = request.session["fid"]
    mappingcourses=FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        #print(course.faculty.facultyid)
        if(course.faculty.facultyid==int(fid)):
            fmcourses.append(course)
    print(fmcourses)
    dir(fmcourses)
    count=len(fmcourses)
    return render(request, "facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})

def facultychangepwd(request):
    fid = request.session["fid"]
    return render(request,"facultychangepwd.html",{"fid":fid})

def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        print("Old Pwd is Correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        msg="Password Updated Successfully"
    else:
        print("Old Password is Incorrect")
        msg="Old Password is Incorrect"
    return render(request,"facultychangepwd.html",{"fid":fid,"message":msg})