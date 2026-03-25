from django.contrib import admin
from .models import Vehicle, Telemetry, DiagnosticResult

admin.site.register(Vehicle)
admin.site.register(Telemetry)
admin.site.register(DiagnosticResult)