from django.shortcuts import render

def aboutUs(request):
    return render(request,"AppAboutUs/aboutUs.html")
