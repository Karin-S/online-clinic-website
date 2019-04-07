from django.urls import path
from django.urls import include
from . import views
from .views import(
    DoctorProfileListView,
    DoctorProfileDetailView,
    AppointmentListView,
    AppointmentDetailView,
    DoctorAppointmentListView,
    DoctorAppointmentDetailView,
    DoctorAppointmentUpdateView,
    DoctorLikeRedirect,
    DoctorLikeAPI,
)

app_name='appointment'
urlpatterns = [
    path('', DoctorProfileListView.as_view(), name='Doctor_ListView'),
    path('<int:id>/', DoctorProfileDetailView.as_view(), name='Doctor_DetailView'),
    path('<int:id>/like', DoctorLikeRedirect.as_view(), name='like'),
    path('api/<int:id>/like', DoctorLikeAPI.as_view(), name='like-api'),
    path('history/', AppointmentListView.as_view(), name='Appointment_ListView'),
    path('history/<int:id>', AppointmentDetailView.as_view(), name='Appointment_DetailView'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('handle_appointment/', DoctorAppointmentListView.as_view(), name='handle_appointment'),
    path('handle_appointment/<int:id>', DoctorAppointmentDetailView.as_view(), name='handle_appointment_detail'),
    path('handle_appointment/<int:id>/update', DoctorAppointmentUpdateView.as_view(), name='appointment_update'),]
