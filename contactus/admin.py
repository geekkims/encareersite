from django.contrib import admin

# Register your models here.

from contactus.models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","phone_number","email_address","message","created_date","updated_date",)
admin.site.register(ContactUs,ContactUsAdmin)