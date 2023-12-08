from django.shortcuts import render,redirect
from Guest.models import UserRegistration #classs from Guest models


# Create your views here.
def homepage(request):
    user=UserRegistration.objects.get(id=request.session["uid"])
    return render(request,"User/Homepage.html",{"un":user})


def myprofile(request):
    user=UserRegistration.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{"un":user})

def editprofile(request):
    user=UserRegistration.objects.get(id=request.session["uid"])
    if request.method=="POST":
        user.name=request.POST.get("ename")
        user.contact=request.POST.get("econtact")
        user.address=request.POST.get("eaddress")
        user.dob=request.POST.get("edob")
        user.save()
        return redirect("webuser:editprofile")
    else:
        return render(request,"User/EditProfile.html",{"un":user})

def changepass(request):
    if request.method=="POST":
        user=UserRegistration.objects.get(id=request.session["uid"])
        pwd=user.password
        crpwd=request.POST.get("curpass")
        if pwd==crpwd:
            npwd=request.POST.get("newpass")
            conpwd=request.POST.get("conpass")
            if npwd==conpwd:
                user.password=npwd
                user.save()
                return redirect("webuser:changepassword")
            else:
                msg="Mismatched new and confimed passwords"
                return render(request,"User/ChangePassword.html",{'msg':msg})
        else:
            msg="Wrong password"
            return render(request,"User/ChangePassword.html",{'msg':msg})
    else:
        return render(request,"User/ChangePassword.html")
    