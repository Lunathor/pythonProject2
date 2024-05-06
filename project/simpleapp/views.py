from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .filers import ProductFilter
from .forms import ProductForm


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 10  # вот так мы указываем кол-во записей на странице
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    
    
class ProductCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'
    
    
class ProductUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'
    
    
class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
