from django.contrib import admin
from .models import Patient, Doctor, Registry, Diagnose, Service, PatientCard, DoctorsEmployment

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'phone_number')
admin.site.register(Patient, PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Doctor, DoctorAdmin)

class RegistryAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'patient_id')
admin.site.register(Registry, RegistryAdmin)

class DiagnosesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Diagnose, DiagnosesAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Service, ServicesAdmin)

class PatientCardAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'patient_id', 'number_of_record', 'dates_of_record')
admin.site.register(PatientCard, PatientCardAdmin)

class DoctorsEmploymentAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'dates_of_records', 'admission_start_time')
admin.site.register(DoctorsEmployment, DoctorsEmploymentAdmin)