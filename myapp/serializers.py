from rest_framework import serializers
from . import models
from account import models as account_models


class DayOfWeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DayofWeek
        fields = '__all__'


class WorkingTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.WorkingTime
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = account_models.CustomUser
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    day_of_week = DayOfWeekSerializer()
    working_time = WorkingTimeSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = models.DoctorsSchedule
        fields = '__all__'
