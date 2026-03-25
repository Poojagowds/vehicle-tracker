from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

from .models import Vehicle

# GLOBAL TRACKING
vehicle_tracking = {}

# ---------------- SIGNUP ----------------
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username exists"})

        if password != confirm:
            return render(request, "signup.html", {"error": "Passwords do not match"})

        User.objects.create_user(username=username, password=password)
        return redirect('/login/')

    return render(request, "signup.html")


# ---------------- VEHICLE LIST ----------------
@login_required(login_url='/login/')
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    return render(request, "vehicle_list.html", {"vehicles": vehicles})


# ---------------- ADD ----------------
@login_required(login_url='/login/')
def add_vehicle(request):
    if request.method == "POST":
        Vehicle.objects.create(
            vehicle_number=request.POST.get("number"),
            model_name=request.POST.get("model"),
            user=request.user
        )
        return redirect('/vehicles/')
    return render(request, "add_vehicle.html")


# ---------------- EDIT ----------------
@login_required(login_url='/login/')
def edit_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id, user=request.user)

    if request.method == "POST":
        vehicle.vehicle_number = request.POST.get("number")
        vehicle.model_name = request.POST.get("model")
        vehicle.save()
        return redirect('/vehicles/')

    return render(request, "edit_vehicle.html", {"vehicle": vehicle})


# ---------------- DELETE ----------------
@login_required(login_url='/login/')
def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id, user=request.user)
    vehicle.delete()
    return redirect('/vehicles/')


# ---------------- DASHBOARD ----------------
@login_required(login_url='/login/')
def dashboard(request, id):
    return render(request, "dashboard.html", {"vehicle_id": id})


# ---------------- LIVE DATA (AI + ALERT) ----------------
def live_data(request):
    vid = int(request.GET.get("id"))

    if vid not in vehicle_tracking:
        vehicle_tracking[vid] = {
            "lat": 12.9716,
            "lon": 77.5946,
            "path": [],
            "temps": []
        }

    v = vehicle_tracking[vid]

    # simulate movement
    v["lat"] += random.uniform(-0.0005, 0.0005)
    v["lon"] += random.uniform(-0.0005, 0.0005)

    v["path"].append([v["lat"], v["lon"]])

    # current temp
    current_temp = random.randint(80, 130)
    v["temps"].append(current_temp)

    if len(v["temps"]) > 5:
        v["temps"].pop(0)

    # AI prediction
    if len(v["temps"]) >= 2:
        diff = v["temps"][-1] - v["temps"][-2]
        predicted_temp = current_temp + diff
    else:
        predicted_temp = current_temp

    # ALERT SYSTEM
    alert = None
    if current_temp > 110:
        alert = "OVERHEATING"
    elif predicted_temp > 110:
        alert = "WARNING: Temperature rising"

    return JsonResponse({
        "engine_temp": current_temp,
        "predicted_temp": predicted_temp,
        "alert": alert,
        "oil_pressure": random.randint(15, 40),
        "battery_voltage": random.randint(10, 14),
        "rpm": random.randint(1000, 4000),
        "speed": random.randint(20, 100),
        "latitude": v["lat"],
        "longitude": v["lon"],
        "path": v["path"],
        "city": random.choice(["Bangalore", "Chennai", "Delhi"])
    })


# ---------------- UPDATE LOCATION ----------------
def update_location(request):
    vid = int(request.GET.get('id'))
    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))

    if vid not in vehicle_tracking:
        vehicle_tracking[vid] = {"lat": lat, "lon": lon, "path": [], "temps": []}

    vehicle_tracking[vid]["lat"] = lat
    vehicle_tracking[vid]["lon"] = lon
    vehicle_tracking[vid]["path"].append([lat, lon])

    return JsonResponse({"status": "updated"})


# ---------------- API ----------------
@api_view(['POST'])
def telemetry_api(request):
    return Response({"message": "API working"})