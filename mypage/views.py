from django.http import HttpResponse
from .models import User
from django.views import generic, View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    user_list = User.objects.order_by('-username')
    context = {'user_list' : user_list}
    return render(request, 'mypage/user_list.html', context)

def detail(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user':user}
    return render(request, 'mypage/user_detail.html', context)

class create(generic.CreateView):
    model = User
    fields = ['username', 'tel', 'email']
    success_url = reverse_lazy('mypage:list')
    template_name_suffix = '_create'