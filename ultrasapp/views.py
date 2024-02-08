from django.shortcuts import render
from ultrasapp.models import *
from admin_app.models import *

# Create your views here.
def index(request):
    obj=sliders.objects.all()
    return render(request,'index.html',{'slider':obj})

def about(request):
    return render(request,'about.html')
def mansonry(request):
    return render(request,'blog-masonry.html')
def sidebar(request):
    return render(request,'blog-sidebar.html')
def blog(request):
    return render(request,'blog.html')
def cart(request):
    return render(request,'cart.html')
def check(request):
    return render(request,'checkout.html')
def coming(request):
    return render(request,'coming-soon.html')
def contact(request):
    return render(request,'contact.html')
def error(request):
    return render(request,'error.html')
def faqs(request):
    return render(request,'faqs.html')
def login(request):
    return render(request,'login.html')
def grid(request):
    return render(request,'shop-grid.html')
def list(request):
    return render(request,'shop-list.html')
def slider(request):
    return render(request,'shop-slider.html')
def shop(request):
    return render(request,'shop.html')
def single_post(request):
    return render(request,'single-post.html')
def single_product(request):
    return render(request,'single-product.html')
def styles(request):
    return render(request,'styles.html')
def thanks(request):
    return render(request,'thank-you.html')
def wishlist(request):
    return render(request,'wishlist.html')




