"""
URL configuration for ultras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ultrasapp.views import *
from admin_app.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    # Website 

    path('',index),
    path('about/',about),
    path('blogmansonry/',mansonry),
    path('blogsidebar/',sidebar),
    path('blog/',blog),
    path('cart/',cart),
    path('checkout/',check),
    path('comingsoon/',coming),
    path('contact/',contact),
    path('error/',error),
    path('faqs/',faqs),
    path('login/',login),
    path('shopgrid/',grid),
    path('shop-list/',list),
    path('shop-slider/',slider),
    path('shop/',shop),
    path('single-post/',single_post),
    path('single-product/',single_product),
    path('styles/',styles),
    path('thank-you/',thanks),
    path('wishlist/',wishlist),


    # Admin_app URLS.....
   
    path('log_in/',log),
    path('ct/',ct),

    # Add slider
    path('slider1/',add_slider),
    path('slider_management/',slider_management),
    path('dashboard/',dashboard),
    path('add_slider/',add_slider),
    path('del_slider/<int:del_id>',del_slider),
    path('upd_slider/<int:upd>',upd_slider),

    # Add Category
    path('category/',category_manegement), 
    path('add_category/',add_category),
    path('upd_cate/<int:up_id>',upd_cate),
    path('del_cate/<int:dl_id>',del_cate),
    

    # Add Product
    path('product/', products),
    path('add_product/', add_product),
    path('upd_pro/<int:uid>', upd_pro),
    path('del_pro/<int:uid>', del_pro),

    

    # Logout
    path('logout/',logout),


    



    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


