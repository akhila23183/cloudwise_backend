from django.urls import path
from .views import upload_csv,client_selection, client_data

urlpatterns = [
    # path('', client_list),
    path('client-data/<int:client_id>/', client_data),

    # path('client-user/',client_user),
    path('upload/',upload_csv),
    path('client-selection/',client_selection)
]