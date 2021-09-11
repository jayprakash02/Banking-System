from django.db import models
import uuid
from rest_framework.serializers import ModelSerializer
# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    cutomer_id=models.UUIDField(default = uuid.uuid4,primary_key=True,auto_created=True)
    wallet=models.FloatField(default=1000.0)
    email=models.EmailField()

    def __str__(self):
        return self.name

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
    
class Transcation(models.Model):
    transcation_id=models.UUIDField(default=uuid.uuid4,primary_key=True,auto_created=True)
    date=models.DateTimeField(auto_now=True)
    to_id=models.ForeignKey(Customer,related_name='to_customer',on_delete=models.CASCADE)
    from_id=models.ForeignKey(Customer,related_name='from_customer',on_delete=models.CASCADE)
    amount=models.FloatField(default=1)
    class Meta:
            ordering=['-date']
    def __str__(self):
        return 'From:{0} | TO:{1} | AMT:{2}'.format(self.from_id.name,self.to_id.name,self.amount)

class TranscationSerializer(ModelSerializer):
    class Meta:
        model = Transcation
        fields = "__all__"