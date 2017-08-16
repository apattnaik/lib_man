from django.db import models

# librarian registration model

class lib_reg(models.Model):
	name= models.CharField(max_length=250)
	gender= models.CharField(max_length=10)
	age= models.IntegerField()
	mobile_no= models.IntegerField()
	

