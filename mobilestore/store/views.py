from django.shortcuts import render,redirect
from .forms import StoreForm,ProductForm
from account.models import User
from .models import ProductModel
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View,TemplateView,CreateView


# Create your views here.
class StoreHome(CreateView):
    template_name="storehome.html"
    Model=User
    form_class=StoreForm
    success_url=reverse_lazy('home')

class AddprdView(CreateView):
    template_name='addproducts.html'
    model=ProductModel
    form_class=ProductForm 
    success_url=reverse_lazy('viewprdt')
        
class ProdView(View):
    def get(self,request):
        prdt=ProductModel.objects.all()
        return render(request,"viewproduct.html",{'data':prdt})
    
    
class DeleteProdct(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        item=ProductModel.objects.get(id=did)
        item.delete()
        return redirect('viewprdt')
    
class EditProduct(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        prdt=ProductModel.objects.get(id=d_id)
        form=ProductForm(instance=prdt) 
        return render(request,"editproduct.html",{'form':form})
    def post(self,request,*args,**kwargs):
        d_did=kwargs.get("did")
        prdt=ProductModel.objects.get(id=d_did)
        form_data=ProductForm(request.POST,files=request.FILES,instance=prdt)
        if form_data.is_valid():
            form_data.save()
            return redirect('viewprdt')
        else:
            return redirect('addprdt')  

          
              

