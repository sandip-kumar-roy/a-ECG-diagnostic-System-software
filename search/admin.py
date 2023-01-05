from django.contrib import admin
from search.models import locate_city
# Register your models here.
admin.site.site_header="My web app"

class locate_cityAdmin(admin.ModelAdmin):  
    list_display = ["name","city","email","phone","address","img"]
    search_fields = ["name","email"]
    list_filter = ["name","email"]

admin.site.register(locate_city,locate_cityAdmin)