from django.db import models

# Create your models here.


class GetQuote(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    business = models.CharField(max_length=100)
    email = models.EmailField(unique=False,max_length=100)
    phone = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100,default="")
    postalCode = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.firstName


class Subscribe(models.Model):
    email = models.EmailField(unique=False)
    created = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False, max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name