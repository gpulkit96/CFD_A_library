from django.contrib import admin
from catalogue.models import Post
#from .models import Post
class PostAdmin(admin.ModelAdmin):
	search_fields = ('id', 'Title', 'Author','Genre','Barcode', )
	list_display = ('Title','id', 'Author','Genre','Barcode', )
admin.site.register(Post,PostAdmin)
# Register your models here.
