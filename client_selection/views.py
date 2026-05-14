# import csv
# import io

#from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import AllowAny
# from rest_framework.decorators import permission_classes
from django.http import JsonResponse

from .models import CloudCost, Client



# @csrf_exempt
# def upload_csv(request):

#     try:

#         csv_file = request.FILES['file']

#         decoded_file = csv_file.read().decode('utf-8-sig').splitlines()

#         reader = csv.DictReader(decoded_file)

#         print("FIELDS:", reader.fieldnames)

#         inserted = 0

#         for row in reader:

#             print("ROW:", row)

#             CloudCost.objects.create(

#                 client_id=row.get('client_id'),
#                 date=row.get('date'),
#                 cloud_provider=row.get('cloud_provider'),
#                 account_id=row.get('account_id'),
#                 service=row.get('service'),
#                 resource_id=row.get('resource_id'),
#                 region=row.get('region'),
#                 usage=row.get('usage'),
#                 cost=row.get('cost'),
#                 currency=row.get('currency'),
#                 team=row.get('team'),
#                 environment=row.get('environment')

#             )

#             inserted += 1

#         return JsonResponse({
#             "message": "uploaded successfully",
#             "inserted": inserted
#         })

#     except Exception as e:

#         print("ERROR:", e)

#         return JsonResponse({
#             "error": str(e)
#         }, status=500)






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
    

def client_user(request):

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    client_data = Client.objects.filter(client=request.user)

    final_data = []

    for c in client_data:

        data = CloudCost.objects.filter(client_id=c.id)

        for i in data:
            final_data.append({
                "id": i.id,
                "client_id": i.client_id,
                "date": str(i.date),
                "cloud_provider": i.cloud_provider,
                "account_id": i.account_id,
                "service": i.service,
                "resource_id": i.resource_id,
                "region": i.region,
                "usage": i.usage,
                "cost": i.cost,
                "currency": i.currency,
                "team": i.team,
                "environment": i.environment
            })

    return JsonResponse(final_data, safe=False)