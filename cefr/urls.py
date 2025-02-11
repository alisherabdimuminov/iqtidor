from django.urls import path

from .views import (
    get_subjects, 
    get_cefrs, 
    get_cefr,
)


urlpatterns = [
    path('subjects/', get_subjects, name='get_subjects'),
    path('subjects/<int:subject_id>/cefrs/', get_cefrs, name='get_cefrs'),
    path('subjects/<int:subject_id>/cefrs/<int:cefr_id>/', get_cefr, name='get_cefr'),
]