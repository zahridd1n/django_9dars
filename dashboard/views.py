from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='dashboard:log-in')
def index(request):
    contacts = models.Contact.objects.all()
    context = {
        'contacts': contacts,
    }

    return render(request, 'dashboard/index.html', context)


"""banner"""


@login_required(login_url='dashboard:log-in')
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


@login_required(login_url='dashboard:log-in')
def list_banner(request):
    banners = models.Head.objects.all()
    context = {
        'banners': banners,
    }
    return render(request, 'dashboard/banner/list.html', context)


@login_required(login_url='dashboard:log-in')
def detail_banner(request, id):
    banner = models.Head.objects.get(id=id)
    context = {
        'banner': banner,
    }
    return render(request, 'dashboard/banner/detail.html', context)


@login_required(login_url='dashboard:log-in')
def edit_banner(request, id):
    banner = models.Head.objects.get(id=id)
    if request.method == 'POST':
        banner.title = request.POST['title']
        banner.description = request.POST['body']
        if request.FILES.get('banner_file'):
            banner.slider_img = request.FILES.get('banner_file')
        banner.save()

    context = {
        'banner': banner,
    }
    return render(request, 'dashboard/banner/edit.html', context)


@login_required(login_url='dashboard:log-in')
def delete_banner(request, id):
    models.Head.objects.get(id=id).delete()
    return redirect('dashboard:list_banner')


"""Aboutus"""


@login_required(login_url='dashboard:log-in')
def create_aboutus(request):
    if request.method == 'POST':
        body = request.POST.get('aboutbody')
        models.About.objects.create(
            body=body,
        )
    return render(request, 'dashboard/aboutus/create.html')


@login_required(login_url='dashboard:log-in')
def list_aboutus(request):
    abouts = models.About.objects.all()
    context = {
        'abouts': abouts,
    }
    return render(request, 'dashboard/aboutus/list.html', context)


@login_required(login_url='dashboard:log-in')
def detail_aboutus(request, id):
    about = models.About.objects.get(id=id)
    context = {
        'about': about,
    }
    return render(request, 'dashboard/aboutus/detail.html', context)


@login_required(login_url='dashboard:log-in')
def edit_aboutus(request, id):
    about = models.About.objects.get(id=id)
    if request.method == 'POST':
        about.body = request.POST['aboutbody']
        about.save()

    context = {
        'about': about,
    }
    return render(request, 'dashboard/aboutus/edit.html', context)


@login_required(login_url='dashboard:log-in')
def delete_aboutus(request, id):
    models.About.objects.get(id=id).delete()
    return redirect('dashboard:list_aboutus')


'''Price '''


@login_required(login_url='dashboard:log-in')
def create_price(request):
    if request.method == 'POST':
        price = request.POST['price']
        status = request.POST['status']
        body = request.POST['body']
        models.Price.objects.create(
            price=price,
            status=status,
            body=body,
        )
    return render(request, 'dashboard/price/create.html', )


@login_required(login_url='dashboard:log-in')
def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices': prices,
    }

    return render(request, 'dashboard/price/list.html', context)


@login_required(login_url='dashboard:log-in')
def detail_price(request, id):
    price = models.Price.objects.get(id=id)
    context = {
        'price': price,
    }
    return render(request, 'dashboard/price/detail.html', context)


@login_required(login_url='dashboard:log-in')
def edit_price(request, id):
    price = models.Price.objects.get(id=id)
    if request.method == 'POST':
        price.price = request.POST['price']
        price.status = request.POST['status']
        price.body = request.POST['body']
        price.save()
        return redirect('dashboard:detail_price', price.id)
    context = {
        'price': price,
    }

    return render(request, 'dashboard/price/edit.html', context)


@login_required(login_url='dashboard:log-in')
def delete_price(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('dashboard:list_price')


"""Service"""

@login_required(login_url='dashboard:log-in')
def create_service(request):
    if request.method == 'POST':
        icon = request.FILES.get('icon')
        name = request.POST.get('name')
        body = request.POST.get('body')
        models.Service.objects.create(
            icon=icon,
            name=name,
            body=body
        )
    return render(request, 'dashboard/service/create.html')


@login_required(login_url='dashboard:log-in')
def list_service(request):
    services = models.Service.objects.all()
    context = {

        'services': services,
    }
    return render(request, 'dashboard/service/list.html', context)


@login_required(login_url='dashboard:log-in')
def detail_service(request, id):
    service = models.Service.objects.get(id=id)
    context = {
        'service': service,
    }
    return render(request, 'dashboard/service/detail.html', context)


@login_required(login_url='dashboard:log-in')
def edit_service(request, id):
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.body = request.POST.get('body')
        if request.FILES.get('icon'):
            service.icon = request.FILES.get('icon')
        service.save()
        return redirect('dashboard:detail_service', service.id)
    context = {
        'service': service,
    }
    return render(request, 'dashboard/service/edit.html', context)


@login_required(login_url='dashboard:log-in')
def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('dashboard:list_service')


"""contact"""


@login_required(login_url='dashboard:log-in')
def list_contact(request):
    contacts = models.Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'dashboard/contact/list.html', context)


@login_required(login_url='dashboard:log-in')
def detail_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    context = {
        'contact': contact,
    }
    return render(request, 'dashboard/contact/detail.html', context)


@login_required(login_url='dashboard:log-in')
def edit_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.is_show = request.POST.get('is_show') == 'on'
        contact.save()
        return redirect('dashboard:detail_contact', contact.id)
    context = {
        'contact': contact,
    }
    return render(request, 'dashboard/contact/edit.html', context)


"""authent"""


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm:
            User.objects.create_user(
                username=username,
                password=password,
            )
            return redirect('dashboard:index')
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return redirect('dashboard:index')
        else:
            ...
    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')
