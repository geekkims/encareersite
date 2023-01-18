from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.core.validators import RegexValidator
from datetime import datetime, timedelta
from django.utils.text import slugify
from django.db.models.signals import pre_save





User = get_user_model()


JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    



class Job(models.Model):

    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    tags = TaggableManager()
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    created_date=models.DateField(auto_now_add=True)
    last_date = models.DateField(default=(datetime.now() + timedelta(days=30)),help_text="By default its set after 30 days but this can be changed")
    is_published = models.BooleanField(default=True)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.add_slug_prefix()
        super().save(*args, **kwargs)
    
    def add_slug_prefix(self):
        if not self.slug:
            self.slug = slugify(self.title)
        prefix = 1
        while Job.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f'{slugify(self.title)}-{prefix}'
            prefix += 1


class Applicant(models.Model):

    
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    phone_number=models.CharField(max_length=300)
    cover_letter=models.FileField(upload_to='cober-letter/',null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])
    resume=models.FileField(upload_to='resumes/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])],help_text="Kindly note only docx and pdf format are allowed")
    expected_salary=models.DecimalField(validators=[RegexValidator(r'^\d+(\.\d{1,2})?$', 'Enter a valid currency number')],max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title

 