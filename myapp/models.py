from django.db import models
import uuid

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, default="")
    gender = models.CharField(max_length=6, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, default="")

class Registry(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Diagnose(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True, default="")

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, default="")

class PatientCard(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    number_of_record = models.IntegerField(unique=True)
    dates_of_record = models.DateField(unique=True)

class DoctorsEmployment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dates_of_records = models.ForeignKey(PatientCard, on_delete=models.CASCADE)
    admission_start_time = models.TimeField(unique=True)
