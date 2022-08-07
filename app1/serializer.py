
from rest_framework import serializers

from.models import customer,foods,category, add_tag, calorie_burnout, customer_view

class create_food_serializer(serializers.ModelSerializer):
    class Meta:
        model = foods
        fields = "__all__"



class create_customer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = "__all__"

class add_tag_serializer (serializers.ModelSerializer):
    class Meta:
        model = add_tag
        fields = "__all__"


class calorie_burnout_serializer(serializers.ModelSerializer):
    class Meta:
        model = calorie_burnout
        fields = "__all__"      


class customer_order_serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_view
        fields = "__all__"
       