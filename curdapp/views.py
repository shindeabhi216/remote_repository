from django.shortcuts import render
from curdapp.models import ProductData
from curdapp.forms import InsertingDataForm,UpdatingDataForm,DelectingDataForm
from django.http.response import HttpResponse

def home(request):
    return render(request,'curd_home.html')


def create_view(request):
    if request.method=="POST":
        #iform=InsertingDataForm(request.POST)
        #if iform.is_valid():
            product_id=request.POST.get('pid')
            product_name=request.POST.get('pname')
            product_cost=request.POST.get('pcost')
            product_class=request.POST.get('pclass')
            no_of_product=request.POST.get('npro')
            manufacture_date=request.POST.get('mdate')
            expiry_date=request.POST.get('edate')
            customer_name=request.POST.get('cname')
            mobile=request.POST.get('mobile')
            email=request.POST.get('eid')

            data=ProductData(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_class=product_class,
                no_of_product=no_of_product,
                manufacture_date=manufacture_date,
                expiry_date=expiry_date,
                customer_name=customer_name,
                mobile=mobile,
                email=email
            )
            data.save()
            #iform=InsertingDataForm()
            return render(request,'insert.html')
        #else:
         #   return HttpResponse("USER MISING VALUES")
    else:
        #iform=InsertingDataForm()
        return render(request,'insert.html')


def retrive_view(request):
    data=ProductData.objects.all()
    return render(request,'retrive.html',{'data':data})


def update_view(request):
    if request.method=="POST":
        product_id=request.POST.get('pid')
        product_cost=request.POST.get('pcost')

        pro_id=ProductData.objects.filter(product_id=product_id)

        if not pro_id:
            return HttpResponse("Product not available")
        else:
            pro_id.update(product_cost=product_cost)
            return render(request,'update.html')
    else:
        return render(request,'update.html')


def delect_view(request):
    if request.method == "POST":
        product_id = request.POST.get('pid')
        pro_id = ProductData.objects.filter(product_id=product_id)

        if not pro_id:
            return ("Product not available")
        else:
            pro_id.delete()
            return render(request, 'delect.html')
    else:
        return render(request, 'delect.html')
