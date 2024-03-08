from django.db import models

class Head(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    slider_img = models.ImageField(upload_to='Slider/', null=True, blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.FileField(upload_to='Service/')
    name = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.name

class About(models.Model):
    body = models.TextField()


class Price(models.Model):
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    status = models.CharField(max_length=20)
    body = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Fotter(models.Model):
    info = models.CharField(max_length=255, blank=True, null=True)
    lacation = models.CharField(max_length=255)
    call_center = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)


