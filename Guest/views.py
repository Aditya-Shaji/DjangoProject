from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
# Create your views here.
def userreg(request):
    district=District.objects.all()
    pdata=Place.objects.all()
    if request.method=="POST"  and request.FILES:
        plac=Place.objects.get(id=request.POST.get("place"))
        UserRegistration.objects.create(
            name=request.POST.get("txtfname"),
            contact=request.POST.get("txtcontact"),
            email=request.POST.get("txtemail"),
            address=request.POST.get("address"),
            file=request.FILES.get("img"),
            dob=request.POST.get("dob"),
            password=request.POST.get("ppassword"),
            place=plac

        )        
        return render(request,"Guest/UserRegistration.html",{'dis':district,'pla':pdata})
    else:
        return render(request,"Guest/UserRegistration.html",{'dis':district,'pla':pdata})
def ajaxplace(request):
    districtdata=District.objects.get(id=request.GET.get('disd'))
    placedata=Place.objects.filter(district=districtdata)
    return render(request,"Guest/Ajaxplace.html",{'data':placedata})


def login(request):
    if request.method=="POST":
        Email = request.POST.get("textemail")
        Password = request.POST.get("password")
        ucount = UserRegistration.objects.filter(email=Email,password=Password).count()
        if ucount > 0:
            userdata = UserRegistration.objects.get(email=Email,password=Password)
            request.session['uid']=userdata.id
            return redirect('user:homepage')
        else:
            msg = "Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'msg':msg})
    else:
        return render(request,"Guest/Login.html")

