from django.shortcuts import render
from myapp import models
from account import models as account_models
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from . import serializers
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, 'myapp/index.html')

def services(request):
    services = models.Service.objects.all()
    return render(request, 'myapp/services.html', {'services': services})

def services_show(request, id):
    service = models.Service.objects.filter(id = id).first()
    return render(request, 'myapp/service_index.html', {'service': service, 'service_id': id})

def about_us(request):
    return render(request, 'myapp/index.html')

def order(request, service_id):
    doctors_group = Group.objects.get(name='doctors')

    doctors = account_models.CustomUser.objects.filter(groups=doctors_group)


    if request.method == 'POST':
        order_time = request.POST.get("order_time")
        service_id = request.POST.get("service")
        service = models.Service.objects.filter(id = service_id).first()
        
        if request.user.id == None:
            return render(request, 'account/login.html')
        patient_id = request.user.id
        patient = account_models.CustomUser.objects.filter(id = patient_id).first()

        doctor_id = request.POST.get("doctor")
        doctor = account_models.CustomUser.objects.filter(id = doctor_id).first()

        print('aaa', type(patient))
        order = models.Order(
                order_time = order_time,
                service = service,
                doctor = doctor,
                patient = patient,
            )

        order_exists = models.Order.objects.filter(
            order_time = order_time,
            service = service,
            doctor = doctor,
        )

        if order_exists.exists():
            return render(request, 'myapp/order.html', context={
                'error': 'Данное время занято',
            })

        order.save()


    return render(request, 'myapp/order.html', context={
        'doctors': doctors,
        'service_id': service_id,
    })



@api_view(['GET'])
def doctor_schedule(request, id):
    schedules = models.DoctorsSchedule.objects.filter(doctor__id = id)
    serializer = serializers.ScheduleSerializer(schedules, many = True)

    return Response(serializer.data)
