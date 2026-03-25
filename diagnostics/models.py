from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20)
    model_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.vehicle_number
class Telemetry(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    engine_temp = models.FloatField()
    oil_pressure = models.FloatField()
    battery_voltage = models.FloatField()
    rpm = models.IntegerField()
    speed = models.FloatField()

    timestamp = models.DateTimeField(auto_now_add=True)


class DiagnosticResult(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    risk_score = models.IntegerField()
    dtc_code = models.CharField(max_length=10)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)