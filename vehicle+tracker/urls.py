from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    # ---------- ADMIN ----------
    path('admin/', admin.site.urls),

    # ---------- DEFAULT REDIRECT ----------
    path('', lambda request: redirect('/login/')),

    # ---------- APP ROUTES ----------
    path('', include('diagnostics.urls')),

    # ---------- AUTH ----------
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='/login/'
    ), name='logout'),
    path('dashboard/', lambda request: redirect('/vehicles/')),
]