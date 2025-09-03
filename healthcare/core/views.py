from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    RegisterSerializer, PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer
)
from .permissions import IsOwnerOrReadOnly

# 1) Auth
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# 2) Patients
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Only patients created by the authenticated user
        return Patient.objects.filter(created_by=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# 3) Doctors
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('last_name', 'first_name')
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# 4) Patient-Doctor Mappings
class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.select_related('patient', 'doctor').all().order_by('-created_at')
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        patient_id = self.kwargs.get('patient_id')
        if patient_id:
            qs = qs.filter(patient_id=patient_id)
        return qs
