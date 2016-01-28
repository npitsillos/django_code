from django.shortcuts import render
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dir = {'categories': category_list}
    return render(request,'rango/index.html',context_dir)

def about(request):
    context_dir = {'message': "Hi"}
    return render(request,'rango/about.html',context_dir)