from django.db import models
from django.forms import ModelForm

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    contact=models.BigIntegerField()
class userForm(ModelForm):
    class Meta:
        model = contact
        fields = ("name","email","password","contact")

class category(models.Model):
    category=models.CharField(max_length=100)
    images=models.FileField(upload_to='media/')

class categoryform(ModelForm):
    class Meta:
        model=category
        fields=["category","images"]


class product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    price=models.IntegerField()
    qty=models.IntegerField()

class productform(ModelForm):
    class Meta:
        model=product
        fields=["title","description","category","price","qty"]
