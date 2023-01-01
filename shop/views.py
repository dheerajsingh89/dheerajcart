from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact
def index(req):
    # products=Product.objects.all()
    # n=len(products)
    # allprod=[[products,range(1,n+1),n],[products,range(1,n+1),n]]
    allprod=[]
    categs=Product.objects.values('category')#getting the categories of all objects
    cats={item["category"] for item in categs}#set comprehension for categories
    for i in cats:
        prod=Product.objects.filter(category=i)#filtering the objects/products according to categories
        n=len(prod)
        allprod.append([prod,range(1,n+1),n])
    dict={'allprods':allprod}
    return render(req,'shop/index.html',dict)
def about(req):
    return render(req,'shop/about.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        print(name)
        email = request.POST.get('email', '')
        print(email)
        phone = request.POST.get('phone', '')
        print(phone)
        desc = request.POST.get('desc', '')
        print(desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        print(contact)
        contact.save()
    return render(request, 'shop/contact.html')
def history(req):
    return render(req,'shop/history.html')
def productview(req,prodid):
    productt=Product.objects.filter(id=prodid)#this will create  a list of only one item(at index 0 ) which is our product of id = prodid
    dict={'product':productt[0]}
    print(productt[0])#print the name of the product that we return in Model class in models.py
    return render(req,"shop/productview.html",dict)
# Create your views here.
