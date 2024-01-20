from django.contrib import admin
from app.models import *
# Register your models here.

class customezeWebpage(admin.ModelAdmin):
   list_display=['topic_name','name','email','url']
   list_display_links=['name']
   list_editable=['url']
   list_filter=['name']
   list_per_page=2
class customezeAccessRecords(admin.ModelAdmin):
   list_display=['name','date','author']
   list_display_links=['author']
   list_editable=['date']
   list_filter=['name']
   



admin.site.register(Topic)
admin.site.register(Webpage,customezeWebpage)
admin.site.register(AccessRecords,customezeAccessRecords)
