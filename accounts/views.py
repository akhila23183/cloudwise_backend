
import csv
import io
import json
 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from .models import CustomUser
from client_selection.models import CloudCost


# REGISTER
@csrf_exempt
def register(request):

    if request.method == "POST":

        data = json.loads(request.body)


        email = data.get("email")

        password = data.get("password")

        confirm_password = data.get("confirm_password")

        if password != confirm_password:

            return JsonResponse({
                "error": "Passwords do not match"
            }, status=400)

        if CustomUser.objects.filter(email=email).exists():

            return JsonResponse({
                "error": "Email already exists"
            }, status=400)

        CustomUser.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        return JsonResponse({
            "message": "User registered successfully"
        })

    return JsonResponse({
        "error": "Only POST allowed"
    })
 

 
 
# LOGIN
@csrf_exempt
def user_login(request):

    if request.method == "POST":

        data = json.loads(request.body)

        email = data.get("email")

        password = data.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user:

            login(request, user)

            return JsonResponse({
                "message": "Login successful"
            })

        return JsonResponse({
            "error": "Invalid credentials"
        }, status=400)

    return JsonResponse({
        "error": "Only POST allowed"
    })
 
# USER DETAILS
 
@csrf_exempt
def user_list(request):
 
    if request.user.is_authenticated:
 
        return JsonResponse({
 
            "id": request.user.id,
        
            "email": request.user.email
 
        })
 
    return JsonResponse({
        "message": "Please login"
    })
 
 

 

