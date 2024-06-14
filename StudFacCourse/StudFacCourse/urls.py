"""
URL configuration for StudFacCourse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",views.homefunction,name="home"),
    path("about",views.aboutfunction,name="about"),
    path("login",views.loginfunction,name="login"),
    path("facultylogin",views.facultylogin,name="facultylogin"),
    path("studentlogin",views.studentlogin,name="studentlogin"),
    path("contactus",views.contactfunction,name="contact"),

    path("",include("adminapp.urls")),
    # path("",include("facultyapp.urls")),
    # path("",include("studentapp.urls")),
]
