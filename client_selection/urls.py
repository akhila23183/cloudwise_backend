from django.urls import path
from .views import client_user

urlpatterns = [
    # path('', client_list),
    # path('<int:client_id>/', client_data),
    path('client_user/',client_user)
]