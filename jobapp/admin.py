from django.contrib import admin
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from jobapp.models import Applicant, Category, Company, Job

# Register your models here.



@receiver(pre_save, sender=Job)
def add_slug_prefix(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    prefix = 1
    while sender.objects.filter(slug=instance.slug).exclude(pk=instance.pk).exists():
        instance.slug = f'{slugify(instance.title)}-{prefix}'
        prefix += 1


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display=('title','created_date','last_date','location','salary')


class CompanyAdmin(admin.ModelAdmin):
    list_display=('company_name','industry')
   




admin.site.register(Job,JobAdmin)
admin.site.register(Category)
admin.site.register(Applicant)
admin.site.register(Company)
