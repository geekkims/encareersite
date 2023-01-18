from django.contrib import admin

from website.models import About, Mainlogo

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
  list_display=('title',)




admin.site.register(Mainlogo)
admin.site.register(About,AboutAdmin)