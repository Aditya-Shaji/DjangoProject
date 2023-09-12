from django.shortcuts import render
from Admin.models import*
# Create your views here.
def district(request):
    if request.method=="POST":
        District.objects.create(name=request.POST.get("district"))
        return render(request,"Admin/District.html")
    else:
        return render(request,"Admin/District.html")
def category(request):
    return render(request,"Admin/Category.html")
def place(request):
    return render(request,"Admin/Place.html")
def sub(request):
    return render(request,"Admin/Subcategory.html")