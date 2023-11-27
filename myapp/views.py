from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def services(request):
    return render(request, 'myapp/services.html')

def about_us(request):
    return render(request, 'myapp/index.html')

def order(request):
    return render(request, 'myapp/order.html')
