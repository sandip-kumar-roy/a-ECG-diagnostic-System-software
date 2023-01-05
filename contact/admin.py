from django.contrib import admin
from contact.models import contact_form
# Register your models here.
class contact_formAdmin(admin.ModelAdmin):
    list_display = ["firstnm","lastnm","mail","contact","mesg"]
admin.site.register(contact_form,contact_formAdmin)

