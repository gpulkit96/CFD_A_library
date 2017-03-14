from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
    search_fields = ('Name','id', 'Status', 'RollNo',)
    list_display = ('Name','id', 'RollNo','Dues','Status')
    list_filter = ('Name','id', 'RollNo','Dues','Status')
    filter_horizontal = ('books',)
admin.site.register(Member,MemberAdmin)

# Register your models here.
