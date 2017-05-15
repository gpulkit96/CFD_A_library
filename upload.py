from catalogue.models import Post
import json
from datetime import datetime, timedelta
import pytz
data =open('list.json')
data1 =json.load(data)
i=0
n=len(data1)
while(i<n):
	post = Post()
	post.Title = data1[i]["TITLE"]
	post.Author=data1[i]["AUTHOR"]
	post.Barcode=data1[i]["BAR CODE"]
	post.Genre=data1[i]["GENRE"]
	post.date= datetime.now(pytz.timezone('Asia/Kolkata'))
	post.save()
	i=i+1