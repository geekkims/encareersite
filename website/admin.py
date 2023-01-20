from django.contrib import admin

from website.models import About, Mainlogo, Offer, Service

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
  list_display=('title',)


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class OfferAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display=('name','created_at','status','slug')




admin.site.register(Mainlogo)
admin.site.register(About,AboutAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Offer,OfferAdmin)