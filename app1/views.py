
from.models import foods,customer,add_tag, calorie_burnout,customer_view
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,status,generics
from. serializer import create_food_serializer,create_customer,add_tag_serializer,calorie_burnout_serializer,customer_order_serializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response

# Create your views here

def home(request):
    return HttpResponse("<h1>Welcome to home page<h1>")

class createfoodview(viewsets.ModelViewSet):
    queryset = foods.objects.all()
    serializer_class = create_food_serializer
    permission_classses = [IsAdminUser]
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data,context={"request":self.request})
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class create_customer(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = customer.objects.all()
    serializer_class = create_customer   


class create_tag(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = add_tag.objects.all()
    serializer_class = add_tag_serializer  


class create_burnout_calorie(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = calorie_burnout.objects.all()
    serializer_class = calorie_burnout_serializer

class customer_order_viewset(viewsets.ModelViewSet):
    queryset = customer_view.objects.all()
    serializer_class = customer_order_serializer
    permission_classses = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # obj = customer_view()
        # obj.save()
        data = request.data
        serializer = self.get_serializer(data=data,context={"request":self.request})
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request,pk=None):
        queryset = customer_view.objects.get(id=pk)
        serializer = self.get_serializer(queryset)
        # burnout = 0
        # if str(queryset.activity_for_burnout) =="cycling":
        #     burnout = float(queryset.time_spend_for_acrivity)*150
        # elif str(queryset.activity_for_burnout) == "walking":
        #     burnout= float(queryset.time_spend_for_acrivity)*50
        # elif str(queryset.activity_for_burnout) == "running":
        #     burnout = float(queryset.time_spend_for_acrivity)*100
        # content = {"burn out":burnout} 
        
        
        return Response(data=serializer.data , status=status.HTTP_200_OK)
        
        
        