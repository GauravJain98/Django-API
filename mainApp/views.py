from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.
  
def show(request,msg):
    return render(request,'show.html',{'msg':msg})

def index(request):
    if request.user.is_authenticated:
        if not Cart.objects.filter(user = request.user):
            c= Cart(user = request.user)
            c.save()
        return redirect('/products')
    else:
        return render(request,'login.html')

def register(request):
    return HttpResponse('register')
def Mylogin(request):
    '''
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)    
                return redirect('/')
        else:
            return HttpsResponse('INVALID')
    '''
    return HttpResponse('login')

def setup(request):
    for i in range(0,100):
        p = Product(name = "Product"+str(i),quantity = (i%5)*4,typeOf= productType[i%4][0],price = 20*(i%5)+20 )
        p.save()
    return HttpResponse('Setup')


def Mylogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def empty(request):
    cart = Cart.objects.get(user = request.user)
    cart.delete()
    cart = Cart(user = request.user)
    cart.save()
    return redirect('/bill')
def addProduct(request,id):
    if request.user.is_authenticated: 
        if request.method == 'POST':
            product = Product.objects.get(id = id)
            quantity = int(request.POST[str('quantity' + str(id))])
            if not Cart.objects.filter(user = request.user):
                c= Cart(user = request.user)
                c.save()
            cart = Cart.objects.get(user = request.user)     
            if product.quantity-quantity <0:
                return show(request,"to much")
            product.quantity = product.quantity-quantity
            product.save()
            cart.amount = int(cart.amount) + int(int(product.price)*quantity)
            cart.save()
            incart = InCart(cart = cart,name = product.name,price = product.price,quantity=quantity)
            incart.save()
        return redirect('/products')
    return redirect('/products')
    
def bill(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user)     
        incart = InCart.objects.filter(cart = cart)
        i = []
        for inc in incart:
            i.append(InCart.objects.get(id = str(inc)))
        return render(request,'bill.html',{'cart':cart,'incart':i})
    else:
        return redirect('/')

def product(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        return render(request,'products.html',{'products':products})
    else:
        return redirect('/')