from rest_framework import serializers
from .models import Vehicle, Telemetry, DiagnosticResult

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class TelemetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetry
        fields = '__all__'


class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticResult
        fields = '__all__'