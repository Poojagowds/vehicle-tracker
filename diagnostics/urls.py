from django.urls import path
from . import views

urlpatterns = [
    # ---------- AUTH ----------
    path('signup/', views.signup, name='signup'),

    # ---------- VEHICLES ----------
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('add/', views.add_vehicle, name='add_vehicle'),
    path('edit/<int:id>/', views.edit_vehicle, name='edit_vehicle'),
    path('delete/<int:id>/', views.delete_vehicle, name='delete_vehicle'),

    # ---------- DASHBOARD ----------
    path('dashboard/<int:id>/', views.dashboard, name='dashboard'),

    # ---------- LIVE TRACKING ----------
    path('live/', views.live_data, name='live_data'),
    path('update-location/', views.update_location, name='update_location'),

    # ---------- API ----------
    path('api/telemetry/', views.telemetry_api, name='telemetry_api'),
]