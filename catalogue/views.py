from django.shortcuts import render
from django.views import generic
from catalogue.models import Post
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from member.models import Member
import requests
import json
import re
import xml.etree.ElementTree as ET
import urllib

class IndexView(generic.ListView):
	template_name="catalogue/catalogue.html"
	def get_queryset(self):
		queryset_list =Post.objects.all().order_by("-date")
		query = self.request.GET.get("q")
		filter_q =  self.request.GET.get("f")
		noviews = self.request.GET.get("i")
		if query:
			if filter_q=="Title":
				queryset_list = queryset_list.filter(Title__icontains =query)
			elif filter_q=="Author":
				queryset_list = queryset_list.filter(Author__icontains =query)
			elif filter_q=="Genre":
				queryset_list = queryset_list.filter(Subject__icontains =query)
			elif filter_q=="CallNum":
				queryset_list = queryset_list.filter(CallNum__icontains =query)
		if noviews=="1-30":
			return queryset_list[:30]
		elif noviews=="1-50":
			return queryset_list[:50]
		elif noviews=="All":
			return queryset_list
		return queryset_list[:15]
class DetailView(generic.DetailView):
	model = Post
	template_name = "catalogue/post.html"

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		title = re.sub("[^\w]", " ",  self.object.Title).split()
		author = re.sub("[^\w]", " ",  self.object.Author).split()
		bTitle = title[0]
		bAuthor = author[0]

		for x in range(1,len(title)):
			bTitle += '+'+ title[x]
		for x in range(1,len(author)):
			bAuthor += '+'+ author[x]

		# url = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search?q='
		# urlend = '&count=2&offset=0&mkt=en-us&safesearch=Off'
		# headers = {'Ocp-Apim-Subscription-Key': '9fd91d75528344cb9b983e7ca664adfd'}
		# r = requests.get(url+(self.object).Title +' book'+ urlend, headers=headers)
		# results = (r.json())["value"][0]
		goodreads_url = 'https://www.goodreads.com/book/title.xml?oauth_signature_method=HMAC-SHA1&oauth_timestamp=1488887063&oauth_nonce=pHIGhp&oauth_version=1.0&oauth_signature=0S3FtoGajPVaW034/TR/CdsTta0=&key=r1kcfqJjWCaypoMLJzPGw&title='+bTitle
		gd = ET.parse(urllib.urlopen(goodreads_url)).getroot()
		context['description'] = gd[1][16].text
		context['rating'] = gd[1][18].text
		context['image_url']= gd[1][8].text
		return context
