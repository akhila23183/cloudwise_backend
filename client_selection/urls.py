from django.urls import path
from .views import upload_csv, clients, client_data

urlpatterns = [
    path('upload/', upload_csv),
    path('clients/', clients),
    path('client/<int:client_id>/', client_data),
]

