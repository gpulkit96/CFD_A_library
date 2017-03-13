from django.db import models
import requests
import json
import re
import xml.etree.ElementTree as ET
import urllib

class Post(models.Model):
	CallNum=models.CharField(max_length=140)
	Barcode=models.CharField(max_length=140)
	Genre=models.CharField(max_length=140)
	Title=models.CharField(max_length=140)
	Author=models.CharField(max_length=140)
	Status=models.CharField(max_length=140, editable=False)
	date=models.DateTimeField(editable=False)
	hidden_date=models.DateTimeField(null=True , editable=False)
	member_Name =models.CharField(max_length=140, editable=False, null=True)
	memberid = models.IntegerField(editable=False, null=True)
	choices = ((0 , 'OK'), (1, 'DUE'))
	duestatus = models.IntegerField(choices = choices, default=0)
	def __str__(self):
		return  self.Title +"_____"+self.CallNum
