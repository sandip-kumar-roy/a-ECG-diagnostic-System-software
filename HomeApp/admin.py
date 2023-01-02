from django.contrib import admin
from HomeApp.models import register_form
# Register your models here.
admin.site.site_header="My web app"

class register_formAdmin(admin.ModelAdmin):
    
    list_display = ["firstname","lastname","username","email","phone","gender","img"]
    search_fields = ["username","email"]
    list_filter = ["firstname","gender"]
    
admin.site.register(register_form,register_formAdmin)