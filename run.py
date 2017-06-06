from catalogue.models import Post
queryset_list =Post.objects.all().order_by("-date")
for book in queryset_list:
	if (book.image==None):
			title = re.sub("[^\w]", " ",  book.Title).split()
			author = re.sub("[^\w]", " ",  book.Author).split()
			p = re.compile(r'<.*?>')
			bTitle = title[0]
			bAuthor = author[0]
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
						book.description = p.sub('', description)

					book.rating = gd.find('average_rating').text
					book.image= gd.find('image_url').text
					book.save()
				except IndexError:
					gd = None

				if (book.image == None):
					book.image= 'https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png'
					book.save()

			except requests.exceptions.ConnectionError:
				status_code = "Connection refused"