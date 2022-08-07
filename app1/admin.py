from django.contrib import admin
from.models import customer,foods,category,add_tag,calorie_burnout,customer_view
# Register your models here.
admin.site.register(customer)
admin.site.register(foods)
admin.site.register(category)
admin.site.register(add_tag)
admin.site.register(calorie_burnout)
admin.site.register(customer_view)