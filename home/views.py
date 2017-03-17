from django.shortcuts import render
import urllib
from catalogue.models import Post
from home.models import Home
from datetime import datetime, timedelta
import pytz
from django.http import HttpResponse
import requests
import json
from django.http import HttpResponseRedirect

def index(request):
	
	return render(request, 'home/home.html')

def bing(request):
	context={}
	if(request.method == 'GET'):
		query = request.GET.get('q')
		print(query,"que")
		if query!=None and query!='':
		
			url = 'https://api.cognitive.microsoft.com/bing/v5.0/search?q='
			urlend = '&count=5&offset=0&mkt=en-us&safesearch=Off'
			headers = {'Ocp-Apim-Subscription-Key': '9fd91d75528344cb9b983e7ca664adfd'}
			try:
				r = requests.get(url + str(query) + urlend, headers=headers)
				webpages = (r.json())["webPages"]["value"]
				l = len(webpages)
				for x in range(l):
					value = webpages[x]
					context['name'+str(x)] = value['name']
					context['url'+str(x)] = value['url']
					context['disp_url'+str(x)] = value['displayUrl']
					context['snippet'+str(x)] = value['snippet']
			except requests.exceptions.ConnectionError:
				status_code = "Connection refused"
						
	return render(request, 'home/bing.html',context)
	
def trending(request):
	context = {}
	books =Post.objects.all().order_by("-date")
	h1 = Home.objects.first()
	date = h1.date
	default_url ='https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png'
	if (datetime.now(pytz.timezone('Asia/Kolkata')) - date).days > 7:
		f = 0
		h1.date = datetime.now(pytz.timezone('Asia/Kolkata'))
		h1.save()
		for book in books:
			url = book.image
			if (url!= None) and (url!=default_url):
				if f==20:
					break
				context['id'+str(f)]=book.id
				urllib.urlretrieve(url, "home/static/home/img/home"+str(f)+".jpg")
				f += 1
		h1.id0 = context['id0']
		h1.id1 = context['id1']
		h1.id2 = context['id2']
		h1.id3 = context['id3']
		h1.id4 = context['id4']
		h1.id5 = context['id5']
		h1.id6 = context['id6']
		h1.id7 = context['id7']
		h1.id8 = context['id8']
		h1.id9 = context['id9']
		h1.id10 = context['id10']
		h1.id11 = context['id11']
		h1.id12 = context['id12']
		h1.id13 = context['id13']
		h1.id14 = context['id14']
		h1.id15 = context['id15']
		h1.id16 = context['id16']
		h1.id17 = context['id17']
		h1.id18 = context['id18']
		h1.id19 = context['id19']
		h1.save()
	else:
		context['id0'] = h1.id0
		context['id1'] = h1.id1
		context['id2'] = h1.id2
		context['id3'] = h1.id3
		context['id4'] = h1.id4
		context['id5'] = h1.id5
		context['id6'] = h1.id6
		context['id7'] = h1.id7
		context['id8'] = h1.id8
		context['id9'] = h1.id9
		context['id10'] = h1.id10
		context['id11'] = h1.id11
		context['id12'] = h1.id12
		context['id13'] = h1.id13
		context['id14'] = h1.id14
		context['id15'] = h1.id15
		context['id16'] = h1.id16
		context['id17'] = h1.id17
		context['id18'] = h1.id18 
		context['id19'] = h1.id19
	return render(request, 'home/trending.html',context)