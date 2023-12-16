from django.views import generic, View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bottoms
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    bottoms_list = Bottoms.objects.order_by('-subject')
    context = {'bottoms_list' : bottoms_list}
    return render(request, 'bottoms/bottoms_list.html', context)

def detail(request, bottoms_id):
    bottoms = Bottoms.objects.get(id=bottoms_id)
    context = {'bottoms':bottoms}
    return render(request, 'bottoms/bottoms_detail.html', context)

class create(generic.CreateView):
    model = Bottoms
    fields = ['subject', 'price', 'explain', 'img']
    success_url = reverse_lazy('bottoms:list')
    template_name_suffix = '_create'

class PaymentView(View):
    def get(self, request, bottoms_id):
        bottoms = Bottoms.objects.get(id=bottoms_id)
        context = {'bottoms': bottoms}
        return render(request, 'bottoms/payment.html', context)
