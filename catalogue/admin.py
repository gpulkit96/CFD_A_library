from django.contrib import admin
from catalogue.models import Post
#from .models import Post
class PostAdmin(admin.ModelAdmin):
    search_fields = ('Barcode','id', 'Title', 'Author','Genre','Barcode', )
    list_display = ('Barcode', 'id','Title', 'Author','Genre', )
    list_filter = ('Barcode', 'id','Title', 'Author','Genre', )
admin.site.register(Post,PostAdmin)
# Register your models here.
