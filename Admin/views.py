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
    variable=Category.objects.all()
    if request.method=="POST":
        Category.objects.create(category=request.POST.get("category"))
        return render(request,"Admin/Category.html")
    else:
        return render(request,"Admin/Category.html",{'cat':variable})
def editcat(request,did):
    editdata=Category.objects.get(id=did)
    Category.objects.get(id=did)
    if request.method=="POST":
        editdata.category=request.POST.get('category')
        editdata.save()
        return redirect("webadmin:catrefresh")
    else:
       return render(request,"Admin/Category.html",{'edit':editdata})

def place(request):
    ddata=District.objects.all()
    pdata=Place.objects.all()
    if request.method=="POST":
        dist=District.objects.get(id=request.POST.get("district"))
        Place.objects.create(district=dist,name=request.POST.get('txtplace'))
        return render(request,"Admin/Place.html",{'district':ddata,'pla':pdata})

    else:        
         return render(request,"Admin/Place.html",{'district':ddata,'pla':pdata})

def subcategory(request):
    cdata=Category.objects.all()
    sdata=Subcategory.objects.all()
    if request.method=="POST":
        print("hai")
        cat=Category.objects.get(id=request.POST.get("category"))
        Subcategory.objects.create(category=cat,name=request.POST.get('subcategory'))
        return render(request,"Admin/Subcategory.html",{'category':cdata,'sub':sdata})
    else:
        return render(request,"Admin/Subcategory.html",{'category':cdata,'sub':sdata})
def delsub(request,did):
   
    Subcategory.objects.get(id=did).delete()
    return redirect("webadmin:subrefresh")
        
    
def delplace(request,did):
   
    Place.objects.get(id=did).delete()
    return redirect("webadmin:plarefresh")
def brand(request):
    variable=District.objects.all()
    if request.method=="POST":
        Brand.objects.create(name=request.POST.get("brand"))
        return render(request,"Admin/Brand.html")
    else:
        return render(request,"Admin/Brand.html",{'brnd':variable})



def adreg(request):
    variable=Register.objects.all()
    if request.method=="POST":
        Register.objects.create(name=request.POST.get("name"),contact=request.POST.get("contact"),email=request.POST.get("email"),password=request.POST.get("password"))
        return render(request,"Admin/AdminRegistration.html")
    else:
        return render(request,"Admin/AdminRegistration.html",{'reg':variable})
