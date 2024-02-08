from django.shortcuts import render,redirect
from admin_app.models import contact,category,categoryform,productform,product
from ultrasapp.models import sliders, obj_slider


# Create your views here.

def log(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    else:
        if 'login' in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            if email == '' or password == '':
                msg = 'Empty Email or Password !'
                return redirect('/log_in',{'msg':msg})
            obj = contact.objects.filter(email=email,password=password)
            msg = ''
            if obj.count() == 1:
                row = obj.get()
                request.session['user_id'] = row.id
                return redirect('/log_in')
            else:
                msg = 'Invalid Email or Password !'
                return redirect('/log_in',{'msg':msg})
    
        return render(request,'login1.html')

def ct(request):
    if 'user_id' in request.session:
        return redirect('/log_in')
    s=''
    if 'save' in request.POST:
        a_name=request.POST['name']
        a_email=request.POST['email']
        a_password=request.POST['password']
        a_contact=request.POST['contact']
        obj=contact(
            name=a_name,
            email=a_email,
            password=a_password,
            contact=a_contact,
        )
        obj.save()  
        s="Created"
        return redirect('/log_in')
    return render(request,'ct.html',{'s':s})

# Dashboard

def dashboard(request):

    user = 'Unknown'

    if 'user_id' not in request.session:
        return redirect('/log_in')
    else:
        obj = contact.objects.filter(id=request.session['user_id']).get()
        user = obj.name
        print(user)

    return render(request,'dashboard.html',{'user':user,'obj':obj})

# Slider

def slider_management(request):

    if 'user_id' not in request.session:
        return redirect('/log_in')
      
    obj = sliders.objects.all()

    return render(request,'slider-management.html',{'obj':obj})

def add_slider(request):

    if 'user_id' not in request.session:
        return redirect('/log_in')
    else:

        btn = 'Add Slider'
        # objslider = obj_slider(request.POST,request.FILES)
        objslider = obj_slider()

        if 'add' in request.POST:
            objslider = obj_slider(request.POST,request.FILES)
            objslider.save()
            return redirect('/slider_management')

    return render(request,'slider.html',{'frm':objslider,'btn':btn})
   
   
def del_slider(request,del_id):

    sliders.objects.filter(id=del_id).delete()

    return redirect('/slider_management')

def upd_slider(request,upd):

    if 'user_id' not in request.session:
        return redirect('/log_in')
    else:
        data = sliders.objects.filter(id=upd).get()
        obj = obj_slider(instance=data)
        
        btn = 'Update Slider'

        if 'add' in request.POST:
            
            obj = obj_slider(request.POST,request.FILES,instance=data)
            obj.save()

            return redirect('/slider1')

    return render(request,'slider.html',{'frm':obj,'btn':btn})


# Category
def category_manegement(request):

    obj = category.objects.all()
    return render(request,'category.html',{'obj':obj})

def add_category(request):

    obj = categoryform()

    if 'add' in request.POST:
        obj = categoryform(request.POST,request.FILES)
        obj.save()
        return redirect('/category')

    return render(request,'add_category.html',{'frm':obj})

def upd_cate(request,up_id):

    data = category.objects.filter(id=up_id).get()
    obj = categoryform(instance=data)
    
    if 'add' in request.POST:
        obj = categoryform(request.POST,request.FILES,instance=data)
        obj.save()
        return redirect('/category')

    return render(request,'add_category.html',{'frm':obj})

def del_cate(request,dl_id):

    category.objects.filter(id=dl_id).delete()

    return redirect('/category')


# Product
def products(request):

    frm = product.objects.all()

    return render(request,'product.html',{'frm':frm})
def add_product(request):

    frm = productform()
    cate = category.objects.all()

    if 'add' in request.POST:
        frm = productform(request.POST,request.FILES)
        frm.save()
        return redirect('/product')

    return render(request,'product.html',{'frm':frm,'cate':cate})
def upd_pro(request,uid):

    data = product.objects.filter(id=uid).get()
    obj = productform(instance=data)
    cate = category.objects.all()

    if 'add' in request.POST:
        obj = productform(request.POST,request.FILES,instance=data)
        obj.save()
        return redirect('/product')

    return render(request,'add_product.html',{'frm':obj,'cate':cate})

def del_pro(request,uid):

    product.objects.filter(id=uid).delete()

    return redirect('/product')

def logout(request):
    del request.session['user_id']
    return redirect('/log_in')