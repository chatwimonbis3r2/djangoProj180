from django.shortcuts import render

def Profile(request):
    return render(request,'Profile.html')

def Education(request):
    return render(request,'Education.html')

def Attention(request):
    return render(request,'Attention.html')

def Career(request):
    return render(request, 'Career.html')

def Product(request):
    return render(request,'Product.html')

def RoleModel(request):
    return render(request,'RoleModel.html')