from django import forms
from django.contrib.auth.models import User
from .models import Profile
from appointment.models import Appointment
from decimal import Decimal

class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'gender','types')

    # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        # Save your profile
        final_rating=0
        profile = Profile()
        profile.user = user
        profile.gender = self.cleaned_data['gender']
        profile.types = self.cleaned_data['types']
        profile.save()

    def get_success_url(self):
        user_id = self.request.Profile.user.id # Get user_id from request
        return reverse_lazy('profiledetail', kwargs={'id': user_id})
