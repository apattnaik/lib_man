from django.db import models
from django.core.urlresolvers import reverse
# books model

class book(models.Model):
	name= models.CharField(max_length=250)
	author= models.CharField(max_length=250)
	category= models.CharField(max_length=250)
	publisher= models.CharField(max_length=250)
	published_date= models.CharField(max_length=250)

	def get_absolute_url(self):
		return reverse('books:detail', kwargs={'pk': self.pk})
		
	def __str__ (self):
		return self.name + '-' + self.author


