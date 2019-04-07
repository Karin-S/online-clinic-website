from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_user")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_user")
    apply_date=models.DateField(auto_now_add=True)
    symptom=models.CharField(max_length=500)
    preferred_time=models.DateField()
    status=models.CharField(max_length=10,default='pending')


    def __str__(self):
        return self.patient.username

    def get_absolute_url(self):
        return reverse("appointment:Appointment_DetailView", kwargs={'id':self.id})
