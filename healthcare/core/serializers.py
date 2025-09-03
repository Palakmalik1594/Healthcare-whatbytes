from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        name = validated_data.pop('name')
        first_name, *rest = name.split(' ', 1)
        last_name = rest[0] if rest else ''
        email = validated_data.get('email')
        username = email  # use email as username
        user = User.objects.create_user(
            username=username,
            email=email,
            password=validated_data['password'],
            first_name=first_name,
            last_name=last_name,
        )
        return user

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','first_name','last_name','age','gender','contact_number','address','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','first_name','last_name','specialization','contact_number','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at']

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source='patient', write_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), source='doctor', write_only=True)

    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient_id', 'doctor_id', 'patient', 'doctor', 'created_at', 'updated_at']
        read_only_fields = ['id','patient','doctor','created_at','updated_at']

    def validate(self, attrs):
        patient = attrs['patient']
        doctor = attrs['doctor']
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError('This doctor is already assigned to the patient.')
        return attrs
