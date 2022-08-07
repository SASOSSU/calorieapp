
from django.urls import path,include
from.import views
from rest_framework import routers
from.views import createfoodview, create_customer,create_tag,create_burnout_calorie,customer_order_viewset,home


router = routers.SimpleRouter()
router.register(r'createfood', createfoodview)
router.register(r'customer_order',customer_order_viewset)

urlpatterns = [
    path('',include(router.urls)),
    path ('create_customer/',create_customer.as_view(),name = "create_customer"),
    path('create_tag/',create_tag.as_view(), name = "create_tag"),
    path ('calories_burnout/',create_burnout_calorie.as_view(),name = "create_burnout"),
    path('home/',home),
]
