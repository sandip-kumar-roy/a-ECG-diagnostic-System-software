from django.contrib import admin
from HomeApp.models import register_form
# Register your models here.
admin.site.site_header="My web app"

class register_formAdmin(admin.ModelAdmin):
    fields=["firstname","lastname","username","email","phone","gender"]
    list_display = ["firstname","lastname","username","email","phone","gender"]
    search_fields = ["username","email"]
    list_filter = ["firstname","gender"]
    list_editable = ["firstname","lastname"]
admin.site.register(register_form)