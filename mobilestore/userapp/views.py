from django.shortcuts import render
from django.views.generic import TemplateView,View
from store.models import ProductModel
from store.forms import ProductForm
from django.urls import reverse_lazy
# Create your views here.
class UserHome(TemplateView):
    template_name="userhome.html"


class ProductView(View):
    model=ProductModel
    form_class=ProductForm
    template_name="productview.html"
    success_url=reverse_lazy('prodview')
    def get(self,request):
        prd=ProductModel.objects.all()
        return render(request,"productview.html",{'data':prd})
