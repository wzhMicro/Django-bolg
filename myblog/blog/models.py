from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Article(models.Model):
	"""docstring for Art"""
	title=models.CharField(max_length=32,default='Title')
	content=models.TextField(null=True)

	def _str_(self):
		return self.title