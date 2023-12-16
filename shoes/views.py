# Create your views here.
from django.http import HttpResponse
from .models import Shoes
from django.views import generic, View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    shoes_list = Shoes.objects.order_by('-subject')
    context = {'shoes_list' : shoes_list}
    return render(request, 'shoes/shoes_list.html', context)

def detail(request, shoes_id):
    shoes = Shoes.objects.get(id=shoes_id)
    context = {'shoes':shoes}
    return render(request, 'shoes/shoes_detail.html', context)

class create(generic.CreateView):
    model = Shoes
    fields = ['subject', 'price', 'explain', 'img']
    success_url = reverse_lazy('bottoms:list')
    template_name_suffix = '_create'

class PaymentView(View):
    def get(self, request, shoes_id):
        shoes = Shoes.objects.get(id=shoes_id)
        context = {'shoes': shoes}
        return render(request, 'shoes/payment.html', context)