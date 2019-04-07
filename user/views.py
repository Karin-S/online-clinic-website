from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseForbidden
from urllib import request
from django.core.exceptions import PermissionDenied

class ProfileUpdate(UpdateView):
    model = User
    fields=['first_name', 'last_name', 'email']
    template_name = 'profile/profile_update.html'

    def get_object(self):
        userid=self.kwargs.get('id')
        if userid==self.request.user.id:
            return get_object_or_404(User, id=userid)
        else:
            raise PermissionDenied

    def get_success_url(self):
        userid=self.kwargs.get('id')
        return reverse("user:profiledetail", kwargs={'id': userid})

class ProfileDetailView(DetailView):
    model = Profile
    fields=['first_name', 'last_name', 'email', 'gender','types']
    template_name = 'profile/profile.html'

    def get_object(self):
        userid=self.kwargs.get('id')
        if userid==self.request.user.id:
            return get_object_or_404(User, id=userid)
        else:
            raise PermissionDenied

def empty(request):
    return render(request, 'profile/profile_empty.html')
