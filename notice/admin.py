from django.contrib import admin
from . models import *

# Register your models here.



class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','notice_by','topic','slug','notification_detail','image','date','viewed','created','updated')
    list_display_links= ('id','notice_by','topic','slug')
    prepopulated_fields = {'slug': ('topic',)}

admin.site.register(Notice, NoticeAdmin)