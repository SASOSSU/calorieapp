
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class customer (TimeStampedModel):
    name = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    code = models.IntegerField()

    def __str__(self):
        return str(self.name)

class category(models.Model):
    options = (('breakfast','breakfast'),('lunch','lunch'),('tea','tea'),('dinner','dinner'))
    name = models.CharField(max_length=30, choices=options)

    def __str__(self):
        return(self.name)

class foods(TimeStampedModel):
    food_name = models.CharField(max_length=40)
    Category = models.ManyToManyField(category)
    calorie = models.DecimalField(max_digits=5,decimal_places=2,default=0, blank=True)

    def __str__(self): 
        return (self.food_name)

class add_tag(models.Model):
    name = models.ForeignKey(foods,on_delete=models.CASCADE)
    tag = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.name)
  
class calorie_burnout(models.Model):
     options = (('running','running'),('walking','walking'),('cycling','cycling'))
     activity = models.CharField(max_length=30, choices=options)
     time = models.FloatField()
     burn_out_calories = models.DecimalField(max_digits=5,decimal_places=2,default=0, blank=True)

     def __str__(self):
         return (self.activity)

class customer_view(models.Model):
    name = models.ForeignKey(customer, on_delete=models.CASCADE)
    food_item_consumed = models.ForeignKey(foods,on_delete=models.CASCADE)
    amount_consumed = models.FloatField()
    activity_for_burnout = models.ForeignKey(calorie_burnout,on_delete=models.CASCADE)
    time_spend_for_acrivity = models.FloatField()
    burnout = models.DecimalField(max_digits=5,decimal_places=2,default=0, blank=True)


    def __int__(self):
         if self.activity_for_burnout =="cycling":
            self.burnout = (self.time_spend_for_acrivity)*150
         elif self.activity_for_burnout == "walking":
            self.burnout= (self.time_spend_for_acrivity)*50
         elif (self.activity_for_burnout) == "running":
            self.burnout = (self.time_spend_for_acrivity)*100
         self.save()
        
        #  super(customer,self).save(*args,**kwargs)    
	
		  

    def __str__(self):
        return str(self.name)

