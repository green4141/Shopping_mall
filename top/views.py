from django.http import HttpResponse
from .models import Top
from django.views import generic, View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    top_list = Top.objects.order_by('-subject')
    context = {'top_list' : top_list}
    return render(request, 'top/top_list.html', context)

def detail(request, top_id):
    top = Top.objects.get(id=top_id)
    context = {'top':top}
    return render(request, 'top/top_detail.html', context)

class create(generic.CreateView):
    model = Top
    fields = ['subject', 'price', 'explain', 'img']
    success_url = reverse_lazy('top:list')
    template_name_suffix = '_create'
    
class PaymentView(View):
    def get(self, request, top_id):
        top = Top.objects.get(id=top_id)
        context = {'top': top}
        return render(request, 'top/payment.html', context)