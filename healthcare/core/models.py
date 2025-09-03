from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Patient(TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=[('male','Male'),('female','Female'),('other','Other')])
    contact_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=20)


    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"


class PatientDoctorMapping(TimeStampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')


    class Meta:
        unique_together = ('patient', 'doctor')