import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .models import CustomUser
 
 
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
 
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
 
        if password != confirm_password:
            return JsonResponse({"error": "Passwords do not match"}, status=400)
 
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)
 
        CustomUser.objects.create_user(email=email, password=password)
 
        return JsonResponse({"message": "User registered successfully"})
 
    return JsonResponse({"error": "Only POST allowed"}, status=405)
 
 
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
 
        email = data.get("email")
        password = data.get("password")
 
        user = authenticate(request, username=email, password=password)
 
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
 
    return JsonResponse({"error": "Only POST allowed"}, status=405)

