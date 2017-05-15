from django.shortcuts import render
from django.views import generic
from member.models import Member
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse

class IndexView(generic.ListView):
	template_name="member/member.html"
	def get_queryset(self):
		all_members = Member.objects.all()
		queryset_list =all_members.order_by("-date")     # sorting all membres by date
		print(all_members)								 # calling all members for updation
		query = self.request.GET.get("q")			
		filter_q =  self.request.GET.get("f")
		noviews = self.request.GET.get("i")
		if query:
			if filter_q=="RollNo":
				queryset_list = queryset_list.filter(RollNo__icontains =query)
			else:
				queryset_list = queryset_list.filter(Name__icontains =query)
		if noviews=="1-30":
			return queryset_list[:30]
		elif noviews=="1-50":
			return queryset_list[:50]
		elif noviews=="All":
			return queryset_list
		return queryset_list[:10]

class DetailView(generic.DetailView):
	model=Member
	template_name="member/post.html"
