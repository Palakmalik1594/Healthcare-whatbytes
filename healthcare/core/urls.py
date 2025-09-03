from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, PatientViewSet, DoctorViewSet, PatientDoctorMappingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'mappings', PatientDoctorMappingViewSet, basename='mapping')

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # CRUD routers
    path('', include(router.urls)),

    # Filter mappings for a specific patient
    path('mappings/patient/<int:patient_id>/',
         PatientDoctorMappingViewSet.as_view({'get': 'list'}),
         name='patient_mappings'),
]
