from django import forms
from django.contrib.auth.models import User
from .models import Appointment
from django.core.exceptions import ValidationError
import datetime


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient','doctor', 'symptom', 'preferred_time')

    # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
    def signup(self, request, patient,doctor):
        patient.username = self.cleaned_data['patient']
        patient.save()
        doctor.username = self.cleaned_data['doctor']
        doctor.save()
        # Save your profile
        appointment = Appointment()
        appointment.patient = patient
        appointment.doctor = doctor
        appointment.symptom = self.cleaned_data['symptom']
        appointment.preferred_time = self.cleaned_data['preferred_time']
        print("here")
        appointment.save()

    def get_success_url(self):
        user_id = self.request.appointment.patient.id # Get user_id from request
        return reverse_lazy('appointment:Appointment_ListView', kwargs={'id': user_id})
