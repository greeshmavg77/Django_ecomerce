from django.utils import timezone
from gc import get_objects
from django.contrib import messages
from .models import cart_Tbl, order_Tbl, orderItem_Tbl, product_Tbl, reg_Tbl
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def home(request):
    return render(request,'home.html')
def user(request):
    return render(request,'user.html')
# register

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=request.POST.get('user')
        obj=reg_Tbl.objects.create(name=name,mobile=mobile,email=email,password=password,user=user)
        obj.save()
        msg='Registion Successfull'
        return render(request,'register.html',{'msg': msg})
    return render(request,'register.html')


# login

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj=reg_Tbl.objects.filter(email=email,password=password)
        
        if obj.exists:
            for i in obj:
                user_id=i.id
                user_name=i.name
                user_mobile=i.mobile
                user_email=i.email
                user_type=i.user
        request.session['id']=user_id
        request.session['name']=user_name
        request.session['mobile']=user_mobile
        request.session['user_type']=user_type
        request.session['email']=user_email
        request.session['password']=password
        
        if user_type=='admin':
            return render(request,'admin.html')
        else:
            return render(request,'user.html')
    return render(request,'login.html')


# productlist

def product(request):
    products=product_Tbl.objects.all()
    return render(request,'product.html',{'products':products})


# add to cart

def addcart(request):
    
    proid=request.GET.get('id_no')
    usr=request.session['id']
    
    p_obj=product_Tbl.objects.get(id=proid)
    c_obj=reg_Tbl.objects.get(id=usr)
    
    cart_item,created=cart_Tbl.objects.get_or_create(fname=c_obj,product_name=p_obj)
    
    if not created:
        cart_item.qty+=1
        cart_item.save()
        
        messages.success(request,'Item added to cart')
        
    return redirect('product')

# view cart

def view_cart(request):
    idno=request.session['id']
    cus_obj=reg_Tbl.objects.get(id=idno)
    cart_obj=cart_Tbl.objects.filter(fname=cus_obj)
    
    if cart_obj:
        total_product_cost=0
        for i in cart_obj:
            total_product_cost+=i.product_name.price * i.qty
            
        return render(request,'view_cart.html',{'cart':cart_obj,'total_product_cost':total_product_cost})
    else:
        return render(request,'view_cart.html',{'info':'your cart is empty'})

# delete

def remove(request):
    id_no=request.GET.get('cid')
    obj=cart_Tbl.objects.filter(id=id_no)
    obj.delete()
    return redirect('view_cart')

# order

def placeorder(request):
    
    idno=request.session.get('id')
    user = reg_Tbl.objects.get(id=idno)

    cart_Items=cart_Tbl.objects.filter(fname=user)
    
    if not cart_Items:
        messages.error(request,'cart is empty')
        return redirect('view_cart')
    
    for item in cart_Items:
        
        total_price=item.product_name.price * item.qty
        order=order_Tbl.objects.create(customer=user,total_price=total_price,order_date=timezone.now())
        
    for item in cart_Items:
        orderItem_Tbl.objects.create(order=order,product=item.product_name,quantity=item.qty,price=item.product_name.price)
    
    
    # delete
    
    cart_Items.delete()
    messages.success(request,"Order placed successfully")
    return render(request,'Order_msg.html',{'order':order})
