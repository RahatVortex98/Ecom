from django.shortcuts import render
from django.views.generic.base import TemplateView


class Store(TemplateView):
    template_name = 'store.html'


class Cart(TemplateView):
    template_name = 'cart.html'
    
class Checkout(TemplateView):
    template_name = 'checkout.html'
    
    
    
    
