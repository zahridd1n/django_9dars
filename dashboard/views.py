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
        file = request.FILES.get('file')
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

def detail_banner(request, id):
    banner = models.Head.objects.get(id=id)
    context = {
        'banner':banner,
    }
    return render(request, 'dashboard/banner/detail.html',context)


def edit_banner(request, id):
        banner = models.Head.objects.get(id=id)
        if request.method == 'POST':
            banner.title = request.POST['title']
            banner.description = request.POST['body']
            if request.FILES.get('banner_file'):
                banner.slider_img = request.FILES.get('banner_file')
            banner.save()

        context = {
            'banner':banner,
        }
        return render(request, 'dashboard/banner/edit.html',context)
def delete_banner(request,id):
   models.Head.objects.get(id=id).delete()
   return redirect('list_banner')



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

def detail_aboutus(request, id):
    about = models.About.objects.get(id=id)
    context = {
        'about':about,
    }
    return render(request, 'dashboard/aboutus/detail.html',context)

def edit_aboutus(request, id):
    about = models.About.objects.get(id=id)
    if request.method == 'POST':
        about.body = request.POST['aboutbody']
        about.save()

    context = {
        'about':about,
    }
    return render(request, 'dashboard/aboutus/edit.html',context)

def delete_aboutus(request,id):
    models.About.objects.get(id=id).delete()
    return redirect('list_aboutus')


'''Price '''

def create_price(request):
    if request.method == 'POST':
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

def detail_price(request, id):
    price = models.Price.objects.get(id=id)
    context = {
        'price':price,
    }
    return render(request, 'dashboard/price/detail.html',context)


def edit_price(request, id):
    price = models.Price.objects.get(id=id)
    if request.method == 'POST':
        price.price = request.POST['price']
        price.status = request.POST['status']
        price.body = request.POST['body']
        price.save()
        return redirect('detail_price', price.id)
    context = {
        'price':price,
    }

    return render(request, 'dashboard/price/edit.html',context)

def delete_price(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('list_price')


"""Service"""

def create_service(request):
    if request.method == 'POST':
        icon = request.FILES.get('icon')
        name = request.POST.get('name')
        body = request.POST.get('body')
        models.Service.objects.create(
            icon = icon,
            name = name,
            body = body
        )
    return render(request, 'dashboard/service/create.html')

def list_service(request):
    services = models.Service.objects.all()
    context ={

       'services':services,
    }
    return render(request, 'dashboard/service/list.html',context)

def detail_service(request, id):
    service = models.Service.objects.get(id=id)
    context = {
       'service':service,
    }
    return render(request, 'dashboard/service/detail.html',context)


def edit_service(request, id):
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.body = request.POST.get('body')
        if request.FILES.get('icon'):
            service.icon = request.FILES.get('icon')
        service.save()
        return redirect('detail_service', service.id)
    context = {
      'service':service,
    }
    return render(request, 'dashboard/service/edit.html',context)

def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('list_service')



"""contact"""

def list_contact(request):
    contacts = models.Contact.objects.all()
    context = {
        'contacts':contacts,
    }
    return render(request, 'dashboard/contact/list.html',context)

def detail_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    context = {
        'contact':contact,
    }
    return render(request, 'dashboard/contact/detail.html',context)

def edit_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.is_show = request.POST.get('is_show')=='on'
        print('on')
        contact.save()
        return redirect('detail_contact', contact.id)
    context = {
        'contact':contact,
    }
    return render(request, 'dashboard/contact/edit.html',context)
