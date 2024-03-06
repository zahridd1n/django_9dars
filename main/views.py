from django.shortcuts import render
from . import models

def index(request):
    head = models.Head.objects.last()
    services = models.Service.objects.all()
    about = models.About.objects.last()
    fotter = models.Fotter.objects.last()

    prices = []
    for i in models.Price.objects.all():
        i.body=i.body.split(',')
        prices.append(i)

    context = {
        'head': head,
        'services': services,
        'about': about,
        'prices': prices,
        'fotter': fotter,

    }
    return render(request, 'front/index.html', context)



def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                message=request.POST.get('message'),
            )
        except:
            ...

    return render(request, 'front/contact.html',context= {'fotter':models.Fotter.objects.last()})



def about(request):
    head = models.Head.objects.last()
    abouts = models.About.objects.last()
    fotter = models.Fotter.objects.last()
    context = {
        'head': head,
        'about': abouts,
        'fotter': fotter,

    }

    return render(request, 'front/about.html',context)


def pricing(request):
    head = models.Head.objects.last()
    fotter = models.Fotter.objects.last()
    prices = []
    for i in models.Price.objects.all():
        i.body = i.body.split(',')
        prices.append(i)

    context = {
        'head':head,
        'prices':prices,
        'fotter':fotter,

    }

    return render(request, 'front/price.html',context)


def service(request):
    head = models.Head.objects.last()
    services = models.Service.objects.all()
    fotter = models.Fotter.objects.last()


    context = {
        'head':head,
        'services':services,
        'fotter':fotter,
    }

    return render(request, 'front/service.html', context)
