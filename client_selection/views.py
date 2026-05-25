import csv
import io
 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import AllowAny
# from rest_framework.decorators import permission_classess
from django.http import JsonResponse
 
from .models import CloudCost, Client
 
 

 
 
 
@csrf_exempt
def upload_csv(request):
 
    if request.method == "POST": 
 
        try:
 
            csv_file = request.FILES['file']
 
            decoded_file = csv_file.read().decode(
                'utf-8'
            ).splitlines()    
 
            # SKIP HEADER
            for row in decoded_file[1:]:
 
                data = [
 
                    x.replace('"', '').strip()
 
                    for x in row.split(',')
 
                ]
 
                print("DATA:", data)
 
                CloudCost.objects.create(
 
                    client_id=int(data[0]),
                    date=data[1],
                    cloud_provider=data[2],
                    account_id=data[3],
                    service=data[4],
                    resource_id=data[5],
                    region=data[6],
                    usage=float(data[7]),
                    cost=float(data[8]),
                    currency=data[9],
                    team=data[10],
                    environment=data[11]
 
                )
 
            return JsonResponse({
 
                "message": "CSV uploaded successfully"
 
            })
 
        except Exception as e:
 
            print("ERROR:", e)
 
            return JsonResponse({
 
                "error": str(e)
 
            })
 
    return JsonResponse({
 
        "message": "Only POST method allowed"
 
    })
 

   
   
 
@csrf_exempt
def client_selection(request):
 
    clients = (
        CloudCost.objects
        .values_list('client_id', flat=True)
        .distinct()
    )
 
    client_list = []
 
    for client in clients:
        client_list.append({
            "client_id": client
        })
 
    return JsonResponse({
        "clients": client_list
    })
   
   
   
 
 
 
@api_view(['GET'])
def client_data(request, client_id):
 
    data = CloudCost.objects.filter( 
        client_id=client_id
    )
 
    result = []
 
    for item in data:
 
        result.append({ 
 
            "id": item.id,
            "client_id": item.client_id,
            "date": str(item.date),
            "cloud_provider": item.cloud_provider,
            "account_id": item.account_id,
            "service": item.service,
            "resource_id": item.resource_id,
            "region": item.region,
            "usage": item.usage,
            "cost": item.cost,
            "currency": item.currency,
            "team": item.team,
            "environment": item.environment
 
        })
 
    return Response({
        "data": result
    })
 