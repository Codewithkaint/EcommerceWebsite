from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product,Contact,Orders,Tracker
import json

def index(request):
    product=Product.objects.all()
    allProbs=[]
    catprods=Product.objects.values('category','id')
   
    cats={item["category"]for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)

        x=n%4
        nSlides=0
        if(x!=0):
            nSlides=1
        nSlides+=n//4
        
        tot=len(product)
   
        
        allProbs.append([prod,range(1,nSlides),tot])

    params={'totProd':allProbs}
    return render(request,'shop/index.html',params)


def about(request):
     return render(request,'shop/about.html')

def tracker(request):
   if request.method=="POST":
        
        email=request.POST.get('email','')
     
        order_id=request.POST.get('order_id','')
        
       

        try:
            obj=Orders.objects.filter(order_id=order_id,email=email)
            
            if(len(obj)>0):
                track_order=Tracker.objects.filter(order_id=order_id)
                orderUpdate=[]
           
                for items in track_order:
                    orderUpdate.append({'text':items.new_desc,"time":items.time})
                
                    respopnse=json.dumps([orderUpdate,obj[0].json],default=str)
                
                return HttpResponse(respopnse)
            else:
                return HttpResponse('{}') 
               
        except:
             return HttpResponse('ex')




   return render(request,'shop/trackers.html')

def checkOut(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        email=request.POST.get('email','')
        name=request.POST.get('name','')
        number=request.POST.get('number','')
        order=request.POST.get('order','')
        add1=request.POST.get('add1','')
        add2=request.POST.get('add2','')
        price=request.POST.get('prices','')
        thank=True
        

        ord=Orders(json=items_json,name=name,email=email,phone=number,order=order,add1=add1,add2=add2,prices=price)
        ord.save()
        track=Tracker(order_id=ord.order_id,new_desc="Order is done")
        track.save()

        return render(request,'shop/checkOut.html',{'check':thank,'id':ord.order_id})
    return render(request,'shop/checkOut.html')




def contact(request):
    if(request.method=="post"):
        print("Hello")
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        item=request.POST.get('item','')
        query=request.POST.get('query','')
        contact=Contact(email=email,phone=number,order=item,query=query)
        contact.save()
       
        
    return render(request,'shop/Contact.html')
def prodView(request,myid):
    product=Product.objects.filter(id=myid)
   
    return render(request,'shop/product.html',{'product':product[0]})


def searchIt(item,query):
    if query.lower() in item.product_name.lower() or query in item.category.lower() or query in item.desc.lower() or query in item.subcategory.lower():
        return True
    else:
        return False



def searchBox(request):
    query=request.GET.get('search')
    
    flag=0
    product=Product.objects.all()
    allProbs=[]
    catprods=Product.objects.values('category','id')
    
    cats={item["category"]for item in catprods}

    for cat in cats:
        prodTemp=Product.objects.filter(category=cat)
        prod=[item for item in prodTemp if searchIt(item,query)]

        n=len(prod)
        print(prod)
        print(n)
        if n>=1:
            flag=1
            print(prod)
        x=n%4
        nSlides=0
        if(x!=0):
            nSlides=1
        nSlides+=n//4
        
        tot=len(product)
   
        
        allProbs.append([prod,range(1,nSlides),tot])
       
    if len(query)<3 or flag==0:
        mesg=""
    else:
        mesg="Pass"
    print(mesg)
    params={'totProd':allProbs,'msg':mesg}
    return render(request,'shop/search.html',params)
