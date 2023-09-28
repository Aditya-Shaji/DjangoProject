from django.shortcuts import render,redirect
#import redirect for deleting
from Admin.models import*
# Create your views here.
def district(request):
    variable=District.objects.all()
    if request.method=="POST":
        District.objects.create(name=request.POST.get("district"))
        return render(request,"Admin/District.html")
    else:
        return render(request,"Admin/District.html",{'dis':variable})
#while delete we run id(did)
def deletedis(request,did):
    variable=District.objects.delete()
    District.objects.get(id=did).delete()
    return redirect("webadmin:districtrefresh")
#edit district
def editdis(request,did):
    editdata=District.objects.get(id=did)
    District.objects.get(id=did)
    if request.method=="POST":
        editdata.name=request.POST.get('district')
        editdata.save()
        return redirect("webadmin:districtrefresh")
    else:
       return render(request,"Admin/District.html",{'edit':editdata})
def category(request):
    if request.method=="POST":
        Catgeory.objects.create(category=request.POST.get("category"))
        return render(request,"Admin/Category.html")
    else:
        return render(request,"Admin/Category.html")
def place(request):
    return render(request,"Admin/Place.html")
def sub(request):
    return render(request,"Admin/Subcategory.html")
def adreg(request):
    variable=Register.objects.all()
    if request.method=="POST":
        Register.objects.create(name=request.POST.get("name"),contact=request.POST.get("contact"),email=request.POST.get("email"),password=request.POST.get("password"))
        return render(request,"Admin/AdminRegistration.html")
    else:
        return render(request,"Admin/AdminRegistration.html",{'reg':variable})
