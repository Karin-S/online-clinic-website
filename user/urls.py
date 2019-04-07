from django.urls import path
from django.urls import re_path
from django.urls import include
from .views import ProfileUpdate
from django.conf.urls import url
from .views import ProfileDetailView
from . import views

app_name='user'
urlpatterns = [
    path('', views.empty,name='profile_empty'),
    path('<int:id>/', ProfileDetailView.as_view(),name='profiledetail'),
    path('<int:id>/update', ProfileUpdate.as_view(),name='profileupdate')]
