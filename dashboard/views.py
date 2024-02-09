from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Brand
from .forms import ProductForm, OrderForm, BrandForm

# Create your views here.

@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    brands = Brand.objects.all()
    brand_count = brands.count()
    product_count = products.count()
    order_count = orders.count()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff = request.user
            instance.save()
            redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders':orders,
        'products':products,
        'brand_count':brand_count,
        'product_count':product_count,
        'order_count':order_count,
        'form':form,
    }
    return render(request,"dashboard/index.html", context)

# @login_required
# def product(request):
#     items = Product.objects.all()
#     form = ProductForm() 

#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             obj=form.save()
#             obj.save()
#             return redirect('dashboard-product')
#     else:
#         form=ProductForm()

#     context={
#         'items':items,
#         'form':form,
#     }
#     return render(request,"dashboard/product.html", context)

@login_required
def brand(request):
    brands = Brand.objects.all()
    brand_count = brands.count()
    form = BrandForm()

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            return redirect('dashboard-brand')  

    context = {
        'brands': brands,
        'brand_count': brand_count,
        'form': form,
    }
    return render(request, "dashboard/brand.html", context)

def brand_delete(request, pk):
    item = Brand.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-brand')
    return render(request, 'dashboard/brand_delete.html')

def brand_update(request, pk):
    item = Brand.objects.get(id=pk)
    if request.method=='POST':
        form = BrandForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-brand')
    else:
        form = BrandForm(instance=item)
    context={
        'form':form,
    }
    return render(request, 'dashboard/brand_update.html',context)

@login_required
def product(request):
    items = Product.objects.all()
    brands = Brand.objects.all()
    product_count = items.count()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()  
            return redirect('dashboard-product')  
        
        
    context={
    'items':items,
    'brands':brands,
    'product_count':product_count,
    'form':form,
    }

    return render(request, 'dashboard/product.html', context)

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context={
        'form':form,
    }
    return render(request, 'dashboard/product_update.html',context)


@login_required
def staff(request):
    return render(request,"dashboard/staff.html")

@login_required
def order(request):
    orders = Order.objects.all()

    context = {
        'orders':orders,
    }
    return render(request,"dashboard/order.html",context)