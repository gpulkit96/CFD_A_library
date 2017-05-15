from django.contrib import admin
from catalogue.models import Post
from django import forms

class MyForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = "__all__" 
		widgets = {'description': forms.Textarea(attrs={'rows':6, 'cols':100}),}
class PostAdmin(admin.ModelAdmin):
	search_fields = ('id', 'Title', 'Author','Genre','Barcode', )
	list_display = ('Title','id', 'Author','Genre','Barcode', )
	form = MyForm
admin.site.register(Post,PostAdmin)

# Register your models here.
