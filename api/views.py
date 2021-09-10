from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status,generics

from rest_framework.views import APIView

from .models import *
# Create your views here.
# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class Details(APIView):
    def get(self,request):
        if self.request.data.__contains__("ID") and Customer.objects.all().filter(cutomer_id=self.request.data["ID"]).exists():
            customer_instance=Customer.objects.get(cutomer_id=self.request.data["ID"])
            details = {'name':customer_instance.name,'ID':customer_instance.cutomer_id,'wallet':customer_instance.wallet,'email':customer_instance.email}
            return Response(details,status=status.HTTP_202_ACCEPTED)
        else :
            return Response('USER NOT FOUND',status=status.HTTP_202_ACCEPTED)

    def post(self,request):
        if self.request.data.__contains__("name") and self.request.data.__contains__("email") :
            customer_instance=Customer.objects.create(name = str(self.request.data["name"]),email=str(self.request.data["email"]))
            customer_instance.save()
            details = {'name':customer_instance.name,'ID':customer_instance.cutomer_id,'wallet':customer_instance.wallet,'email':customer_instance.email}
            return Response(details,status=status.HTTP_201_CREATED)
    
            
class Transfer(APIView):
    def get(self,request,*args, **kwargs):
        transction={}
        print(self.request.query_params)
        if self.request.query_params.__contains__("ID") and Customer.objects.all().filter(cutomer_id=self.request.query_params["ID"]).exists():
            customer_instance=Customer.objects.get(cutomer_id=self.request.query_params["ID"])
            # for i in customer_instance.to_customer:
            credit = TranscationSerializer(customer_instance.to_customer,many=True)
            transfer = TranscationSerializer(customer_instance.from_customer,many=True)
            transction = {'credit':credit.data,'transfer':transfer.data}
            return Response(transction,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(transction,status=status.HTTP_204_NO_CONTENT)
            

    def post(self,request):
        if self.request.data.__contains__("FROM") and self.request.data.__contains__("TO") and self.request.data.__contains__("AMOUNT"):
            from_id=self.request.data["FROM"]
            to_id=self.request.data["TO"]
            amt=float(self.request.data["AMOUNT"])
            if Customer.objects.all().filter(cutomer_id=from_id).exists and Customer.objects.all().filter(cutomer_id=to_id).exists:
                from_instance=Customer.objects.get(cutomer_id=from_id)
                to_instance=Customer.objects.get(cutomer_id=to_id)
                if amt<=from_instance.wallet :
                    from_instance.wallet-=amt
                    to_instance.wallet+=amt
                    from_instance.save()
                    to_instance.save()
                    Transcation.objects.create(to_id=to_instance,from_id=from_instance,amount=amt)
                    return Response('Transaction Success !!',status=status.HTTP_202_ACCEPTED)
                else :
                    return Response('You Donnot have enough amount !!',status.HTTP_406_NOT_ACCEPTABLE)
            else :
                return Response('Customer Does not exist !!', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Bad Request',status=status.HTTP_400_BAD_REQUEST)

class CustomerList(generics.ListAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
