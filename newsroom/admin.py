from django.contrib import admin
from newsroom.models import newsdata

# Register your models here.
class newsdataAdmin(admin.ModelAdmin):
     list_display=['head','body']   

admin.site.register(newsdata)
