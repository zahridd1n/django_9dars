from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


@login_required(login_url='dashboard:log-in')
def index(request):
    contacts = models.Contact.objects.all()
    banners = models.Head.objects.all()
    services = models.Service.objects.all()
    prices = models.Price.objects.all()
    context = {
        'contacts': contacts,
        'banners': banners,
        'prices': prices,
        'services': services,
    }

    return render(request, 'dashboard/index.html', context)


"""banner"""


@login_required(login_url='dashboard:log-in')
def create_banner(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            body = request.POST.get('body')
            file = request.FILES.get('file')
            models.Head.objects.create(
                title=title,
                description=body,
                slider_img=file,

            )
            messages.success(request, 'Banner yaratildi')
        except:
            messages.error(request, 'Banner yaratilishda xatolik')

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
        try:
            banner.title = request.POST['title']
            banner.description = request.POST['body']
            if request.FILES.get('banner_file'):
                banner.slider_img = request.FILES.get('banner_file')
            banner.save()
            messages.success(request, 'Bannerni tahrirlandi')
        except:
            messages.error(request, 'Bannerni tahrirlashda xatolik')

        return redirect('dashboard:detail_banner', banner.id)

    context = {
        'banner': banner,
    }
    return render(request, 'dashboard/banner/edit.html', context)


@login_required(login_url='dashboard:log-in')
def delete_banner(request, id):
    models.Head.objects.get(id=id).delete()
    messages.success(request, 'bannner muvafaqiyatki o`chirildi')
    return redirect('dashboard:list_banner')


@login_required(login_url='dashboard:log-in')
def create_aboutus(request):
    """Aboutus"""
    if request.method == 'POST':
        try:
            body = request.POST.get('aboutbody')
            models.About.objects.create(
                body=body,
            )
            messages.success(request, 'yangi about yaratildi')
        except:
            messages.error(request, 'about yaratishda xatoli yuzaga keldi')

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
    context = {
        'about': about,
    }

    if request.method == 'POST':
        try:
            about.body = request.POST['aboutbody']
            about.save()
            messages.success(request, 'about tahrirlandi')
        except:
            messages.error(request, 'aboutni tahrirlashda xatolik')

        return redirect('dashboard:detail_aboutus', about.id)

    return render(request, 'dashboard/aboutus/edit.html', context)


@login_required(login_url='dashboard:log-in')
def delete_aboutus(request, id):
    models.About.objects.get(id=id).delete()
    messages.success(request, 'about muvafaqiyatli o`chirildi')
    return redirect('dashboard:list_aboutus')


'''Price '''


@login_required(login_url='dashboard:log-in')
def create_price(request):
    if request.method == 'POST':
        try:
            price = request.POST['price']
            status = request.POST['status']
            body = request.POST['body']
            models.Price.objects.create(
                price=price,
                status=status,
                body=body,
            )
            messages.success(request, 'Price yaratildi')
        except:
            messages.error(request, 'Price yaratishda xatoli yuzaga keldi')
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
    messages.success(request, 'Price muvafaqiyatli o`chirildi')
    return redirect('dashboard:list_price')


"""Service"""


@login_required(login_url='dashboard:log-in')
def create_service(request):
    if request.method == 'POST':
        try:
            icon = request.FILES.get('icon')
            name = request.POST.get('name')
            body = request.POST.get('body')
            models.Service.objects.create(
                icon=icon,
                name=name,
                body=body
            )
            messages.success(request, 'Service yaratildi')
        except:
            messages.error(request, 'Service yaratishda xatoli yuzaga keldi')
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
    context = {
        'service': service,
    }
    if request.method == 'POST':
        try:
            service.name = request.POST.get('name')
            service.body = request.POST.get('body')
            if request.FILES.get('icon'):
                service.icon = request.FILES.get('icon')
            service.save()
            messages.success(request, 'Service tahrirlandi')
        except:
            messages.error(request, 'Serviceni tahrirlashda xatolik bor')
        return redirect('dashboard:detail_service', service.id)
    return render(request, 'dashboard/service/edit.html', context)


@login_required(login_url='dashboard:log-in')
def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    messages.success((request, ("Service muvafaqiyatli o'chirildi")))
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
    context = {
        'contact': contact,
    }
    if request.method == 'POST':
        try:
            contact.is_show = request.POST.get('is_show') == 'on'
            contact.save()
            messages.success(request, 'Contact tahrirlandi')
            return redirect('dashboard:detail_contact', contact.id)
        except:
            messages.error(request, 'Contactni tahrirlashda xatolik bor')
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
            messages.success(request, 'User yaratildi')
            user = authenticate(
                username=username,
                password=password,
            )
            if user:
                login(request, user)
            return redirect('dashboard:index')

        else:

            messages.error(request, 'User yaratishda xatoli yuzaga keldi')
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
            messages.success(request, 'Kirish amalga to`gri amalga oshdi')
            return redirect('dashboard:index')
        else:
            messages.error(request, 'kirishda xatolik, qayta urinib ko\'ring ')
    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')


def query(request):
    q=request.GET['q']
    banners = models.Head.objects.filter(Q(title__icontains=q)|Q(description__icontains=q))
    services = models.Service.objects.filter(name__icontains=q)
    prices = models.Price.objects.filter(Q(status__icontains=q)|Q(body__icontains=q))
    contacts = models.Contact.objects.filter(Q(name__icontains=q)|Q(phone__icontains=q))
    context={
        'banners':banners,
        'prices':prices,
        'contacts':contacts,
        'services':services,
    }

    return render(request,'dashboard/query.html',context)
