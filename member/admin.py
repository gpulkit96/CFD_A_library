from django.contrib import admin
from member.models import Member
from catalogue.models import Post
from django import forms
from itertools import chain

class MemberAdmin(admin.ModelAdmin):
	def formfield_for_manytomany(self, db_field, request, **kwargs):
		if db_field.name == "books":
			try:
				self_pub_id = request.resolver_match.args[0]
				query1 = Post.objects.filter(memberid=None)
				query2 = Post.objects.filter(memberid=self_pub_id)
				kwargs["queryset"] =query2 | query1
			except IndexError:
				query1 = Post.objects.filter(memberid=None)
				kwargs["queryset"] =query1
		return super(MemberAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
	search_fields = ('Name','id', 'RollNo',)
	list_display = ('Name','id', 'RollNo','EmailID', 'Fine','Slots',)
	filter_horizontal = ('books',)
admin.site.register(Member,MemberAdmin)

# Register your models here.
