from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import RedirectView
from user.models import Profile
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Appointment
from django.shortcuts import render
from .forms import AppointmentForm
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from urllib import request
from decimal import Decimal

class DoctorProfileListView(ListView):
    queryset=User.objects.all()
    template_name = 'appointment/appointment.html'

class DoctorAppointmentListView(ListView):
    queryset=Appointment.objects.all()
    template_name = 'appointment/handle_appointment.html'

class DoctorProfileDetailView(DetailView):
    queryset=User.objects.all()
    template_name = 'appointment/appointment_detail.html'

    def get_object(self):
        userid= self.kwargs.get("id")
        return get_object_or_404(User, id=userid)

class DoctorLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        doctorid=self.kwargs.get("id")
        obj=get_object_or_404(User, id=doctorid)
        current_user=self.request.user
        if current_user.is_authenticated:
            if current_user in obj.profile_user.likes.all():
                obj.profile_user.likes.remove(current_user)
            else:
                obj.profile_user.likes.add(current_user)
        return reverse("appointment:Doctor_DetailView", kwargs={'id': doctorid})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated


class DoctorLikeAPI(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None, format=None):
        #doctorid=self.kwargs.get("id")
        obj=get_object_or_404(User, id=id)
        current_user=self.request.user
        updated=False
        liked=False
        if current_user.is_authenticated:
            if current_user in obj.profile_user.likes.all():
                liked=False
                obj.profile_user.likes.remove(current_user)
            else:
                liked=True
                obj.profile_user.likes.add(current_user)
            updated=True
        data={
            "updated": updated,
            "liked": liked
        }
        return Response(data)


class DoctorAppointmentUpdateView(UpdateView):
    model = Appointment
    fields=['status']
    template_name = 'appointment/appointment_update.html'

    def get_object(self):
        appointmentid=self.kwargs.get('id')
        userid=self.request.user.id
        appointment_model = Appointment.objects.get(id=appointmentid)
        if appointment_model.doctor.id==userid:
            return get_object_or_404(Appointment, id=appointmentid)
        else:
            raise PermissionDenied


    def get_success_url(self):
        return reverse("appointment:handle_appointment")

class DoctorAppointmentDetailView(DetailView):
    queryset=Appointment.objects.all()
    template_name = 'appointment/handle_appointment_detail.html'

    def get_object(self):
        appointmentid= self.kwargs.get("id")
        return get_object_or_404(Appointment, id=appointmentid)

class AppointmentListView(ListView):
    queryset=Appointment.objects.all()
    template_name = 'appointment/appointment_history.html'

class AppointmentDetailView(DetailView):
    queryset=Appointment.objects.all()
    template_name = 'appointment/appointment_history_detail.html'

    def get_object(self):
        appointmentid=self.kwargs.get('id')
        userid=self.request.user.id
        appointment_model = Appointment.objects.get(id=appointmentid)
        if appointment_model.patient.id==userid:
            return get_object_or_404(Appointment, id=appointmentid)
        else:
            raise PermissionDenied


def make_appointment(request):
    doctors = Profile.objects.filter(types="Doctor")
    if request.method == 'post' or request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('appointment:Appointment_ListView') )
    else:
        form = AppointmentForm()
    return render(request, 'appointment/make_appointment.html', {'doctors':doctors,'form': form})
