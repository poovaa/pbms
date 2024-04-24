from django.db import models

# Create your models here.

class Doner(models.Model):
	
	Name=models.TextField()
	Bloodbank=models.TextField()
	District=models.TextField()
	Number=models.BigIntegerField()
	Email=models.TextField()
	Password=models.TextField()
	BloodGroup=models.TextField()

class Meta:
	db_table='doner'
    
	
