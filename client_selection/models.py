from django.db import models
from accounts.models import CustomUser

class CloudCost(models.Model):
    client_id = models.IntegerField(null=False)
    date = models.DateField()
    cloud_provider = models.CharField(max_length=100)
    account_id = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    resource_id = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    usage = models.FloatField()
    cost = models.FloatField()
    currency = models.CharField(max_length=10)
    team = models.CharField(max_length=100)
    environment = models.CharField(max_length=100)
    
    
    class Meta:
        db_table = "cloudwise_cloudcost"
        
class client(models.Model):
    client = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
