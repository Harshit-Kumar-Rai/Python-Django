from django.shortcuts import render, redirect
from .models import Data

def index(request):
    return render (request, 'register.html')

def insert_data(request):
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    address = request.POST.get('address')
    
    insert_data = Data.objects.create(name = name,
                                      contact = contact,
                                      email = email,
                                      address = address)
    insert_data.save()
    return redirect('fetch_data')

def fetch_data(request):
    user_data = Data.objects.all()
    
    return render(request, 'show.html',{'data':user_data})

def edit_data(request,pk):
    update = Data.objects.get(id=pk)
    return render(request, 'edit.html',{'update':update})

def update_data(request, pk):
    udata = Data.objects.get(id=pk)
    
    udata.name = request.POST.get('name')
    udata.contact = request.POST.get('contact')
    udata.email = request.POST.get('email')
    udata.address= request.POST.get('address')
    udata.save()
    
    return redirect('fetch_data')

def delete_data(request, pk):
    d_data = Data.objects.get(id=pk)
    d_data.delete()
    return redirect('fetch_data')
    