from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','age','gender','created_by','created_at')
    search_fields = ('first_name','last_name','contact_number')
    list_filter = ('gender',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','specialization','contact_number')
    search_fields = ('first_name','last_name','specialization')

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('id','patient','doctor','created_at')
    list_select_related = ('patient','doctor')
