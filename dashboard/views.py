from django.shortcuts import render,redirect
from main import models

def index(request):
    contacts = models.Contact.objects.all()
    context = {
   'contacts':contacts,
    }

    return render(request,'dashboard/index.html',context)



"""banner"""

def create_banner(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        file = request.POST.get('file')
        models.Head.objects.create(
            title=title,
            description=body,
            slider_img=file,

        )
    return render(request, 'dashboard/banner/create.html')

def list_banner(request):
    banners = models.Head.objects.all()
    context = {
        'banners':banners,
    }
    return render(request, 'dashboard/banner/list.html',context)


"""Aboutus"""

def create_aboutus(request):

    if request.method == 'POST':
        body = request.POST.get('aboutbody')
        models.About.objects.create(
            body=body,
        )
    return render(request, 'dashboard/aboutus/create.html')


def list_aboutus(request):
    abouts = models.About.objects.all()
    context = {
        'abouts':abouts,
    }
    return render(request, 'dashboard/aboutus/list.html',context)



'''Price '''

def create_price(request):
    if request.method =='POST':
        price = request.POST['price']
        status = request.POST['status']
        body = request.POST['body']
        models.Price.objects.create(
            price = price,
            status = status,
            body = body,
        )
    return render(request, 'dashboard/price/create.html',)

def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices,
    }

    return render(request, 'dashboard/price/list.html',context)



"""Service"""

def create_service(request):
    if request.method == 'POST':
        icon = request.POST.get('icon')
        name = request.POST.get('name')
        body = request.POST.get('body')
        models.Service.objects.create(
            icon = icon,
            name = name,
            body = body,
        )
    return render(request, 'dashboard/service/create.html')

def list_service(request):
    services = models.Service.objects.all()
    context ={

       'services':services,
    }
    return render(request, 'dashboard/service/list.html',context)