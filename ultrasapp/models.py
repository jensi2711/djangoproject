from django.db import models
from django.forms import ModelForm

# Create your models here.
class sliders(models.Model):
    title=models.CharField(max_length=150)
    meta=models.CharField(max_length=150)
    image=models.FileField(upload_to='media/')


class obj_slider(ModelForm):
    class Meta:
        model=sliders
        fields=["title","meta","image"]
    
