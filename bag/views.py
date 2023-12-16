from django.views import generic, View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bag
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    bag_list = Bag.objects.order_by('-subject')
    context = {'bag_list' : bag_list}
    return render(request, 'bag/bag_list.html', context)

def detail(request, bag_id):
    bag = Bag.objects.get(id=bag_id)
    context = {'bag':bag}
    return render(request, 'bag/bag_detail.html', context)

class create(generic.CreateView):
    model = Bag
    fields = ['subject', 'price', 'explain', 'img']
    success_url = reverse_lazy('bag:list')
    template_name_suffix = '_create'

class PaymentView(View):
    def get(self, request, bag_id):
        bag = Bag.objects.get(id=bag_id)
        context = {'bag': bag}
        return render(request, 'bag/payment.html', context)