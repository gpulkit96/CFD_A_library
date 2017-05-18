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
from django import forms

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
				queryset_list = queryset_list.filter(Genre__icontains =query)
			elif filter_q=="Call Num":
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