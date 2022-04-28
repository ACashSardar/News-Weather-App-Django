from django.contrib import admin
from .models import YTClist

# Register your models here.
@admin.register(YTClist)
class YTClistAdmin(admin.ModelAdmin):
    list_display=['id','url']