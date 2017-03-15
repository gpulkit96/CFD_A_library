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
	date=models.DateTimeField(editable=False)
	hidden_date=models.DateTimeField(null=True , editable=False)
	member_Name =models.CharField(max_length=140, editable=False, null=True)
	memberid = models.IntegerField(editable=False, null=True)
	choices = ((0 , 'OK'), (1, 'DUE'))
	duestatus = models.IntegerField(choices = choices, default=0)
	image = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=2000, null=True)
	rating = models.CharField(max_length=100,null=True)

	def __str__(self):
		title = re.sub("[^\w]", " ",  self.Title).split()
		author = re.sub("[^\w]", " ",  self.Author).split()
		p = re.compile(r'<.*?>')
		bTitle = title[0]
		bAuthor = author[0]
		if (self.image==None) or (self.description==None):

			for x in range(1,len(title)):
				bTitle += '+'+ title[x]
			for x in range(1,len(author)):
				bAuthor += '+'+ author[x]
			url = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search?q='
			urlend = '&count=2&offset=0&mkt=en-us&safesearch=Off'
			headers = {'Ocp-Apim-Subscription-Key': '9fd91d75528344cb9b983e7ca664adfd'}
			try:
	   			r = requests.get('https://github.com')
				goodreads_url = 'https://www.goodreads.com/book/title.xml?oauth_signature_method=HMAC-SHA1&oauth_timestamp=1488887063&oauth_nonce=pHIGhp&oauth_version=1.0&oauth_signature=0S3FtoGajPVaW034/TR/CdsTta0=&key=r1kcfqJjWCaypoMLJzPGw&title='+bTitle+'&author='+bAuthor
				gd = ET.parse(urllib.urlopen(goodreads_url)).getroot()
				if gd.tag=="error":
					goodreads_url = 'https://www.goodreads.com/book/title.xml?oauth_signature_method=HMAC-SHA1&oauth_timestamp=1488887063&oauth_nonce=pHIGhp&oauth_version=1.0&oauth_signature=0S3FtoGajPVaW034/TR/CdsTta0=&key=r1kcfqJjWCaypoMLJzPGw&title='+bTitle
					gd = ET.parse(urllib.urlopen(goodreads_url)).getroot()
				try:
					gd = gd[1]
					description =  gd.find('description').text
					if description!= None:
						self.description = p.sub('', description)
					
					self.rating = gd.find('average_rating').text
					self.image= gd.find('image_url').text
					self.save()
				except IndexError:
					gd = None
    			
			
			except requests.exceptions.ConnectionError:
				status_code = "Connection refused"
		return  self.Title +"_____"+self.CallNum
