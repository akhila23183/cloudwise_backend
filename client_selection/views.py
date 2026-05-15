import csv
import io

#from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import AllowAny
# from rest_framework.decorators import permission_classes
from django.http import JsonResponse

from .models import CloudCost, Client


@csrf_exempt
def upload_csv(request):

    if request.method == "POST":

        try:

            csv_file = request.FILES['file']

            decoded_file = csv_file.read().decode('utf-8').splitlines()

            reader = csv.reader(decoded_file)

            next(reader)

            for row in reader:  

                # split manually
                data = row[0].split(',')

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

            return JsonResponse({
                "error": str(e)
            })

    return JsonResponse({
        "message": "Only POST method allowed"
    })







# # @api_view(['GET'])
# # def clients(request):

# #     clients = CloudCost.objects.values_list(
# #         'client_id',
# #         flat=True
#     ).distinct()

#     return Response({
#         "clients": list(clients)
#     })
        
        
# @api_view(['GET'])
# def client_data(request, client_id):

#     data = CloudCost.objects.filter(
#         client_id=client_id
#     )

#     result = []

#     for item in data:

#         result.append({
            
#             "id": item.id,
#             "client_id": item.client_id,
#             "date": item.date,
#             "cloud_provider": item.cloud_provider,
#             "account_id": item.account_id,
#             "service": item.service,
#             "resource_id": item.resource_id,
#             "region": item.region,
#             "usage": item.usage,
#             "cost": item.cost,
#             "currency": item.currency,
#             "team": item.team,
#             "environment": item.environment

#         })

#     return Response(result)
# def Client_data(request):
#     data = client.objects.all()

# def client_list(request):

#     clients = client.objects.select_related('client').all()

#     data = []

#     for i in clients:
#         data.append({
#             "client_id": i.id,
#             "email": i.client.email,
#         })

#     return JsonResponse({
#         "clients": data
#     })
    




# def client_data(request, client_id):

#     print("CLIENT ID:", client_id)

#     data = CloudCost.objects.filter(client_id=client_id)

#     print("QUERYSET:", data)
#     print("COUNT:", data.count())

#     final_data = []

#     for i in data:

#         print(i.id, i.cloud_provider)

#         final_data.append({
#             "id": i.id,
#             "client_id": i.client_id,
#             "date": str(i.date),
#             "cloud_provider": i.cloud_provider,
#             "account_id": i.account_id,
#             "service": i.service,
#             "resource_id":i.resource_id,
#             "region":i.region,
#             "usage":i.usage,
#             "cost": i.cost,
#             "currency": i.currency,
#             "team":i.team,
#             "environment": i.environment

#         })

#     return JsonResponse({
#         "client_id": client_id,
#         "data": final_data
#     })
    

# def client_user(request):

#     if not request.user.is_authenticated:
#         return JsonResponse({"error": "Unauthorized"}, status=401)

#     client_data = Client.objects.filter(client=request.user)

#     final_data = []

#     for c in client_data:

#         data = CloudCost.objects.filter(client_id=c.id)

#         for i in data:
#             final_data.append({
#                 "id": i.id,
#                 "client_id": i.client_id,
#                 "date": str(i.date),
#                 "cloud_provider": i.cloud_provider,
#                 "account_id": i.account_id,
#                 "service": i.service,
#                 "resource_id": i.resource_id,
#                 "region": i.region,
#                 "usage": i.usage,
#                 "cost": i.cost,
#                 "currency": i.currency,
#                 "team": i.team,
#                 "environment": i.environment
#             })

#     return JsonResponse(final_data, safe=False)


    

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