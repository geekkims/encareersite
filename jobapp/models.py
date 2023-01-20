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


SALARY_RANGE_CHOICES = (
('Confidential', 'Confidential'),
(10000, '10,000 - 30,000 KES'),
(31000, '31,000 - 60,000 KES'),
(61000, '61,000 - 90,000 KES'),
(91000, '91,000 - 120,000 KES'),
(121000, '121,000 - 150,000 KES'),
(151000, '151,000 - 180,000 KES'),
(181000, '181,000 - 210,000 KES'),
(211000, '211,000 - 240,000 KES'),
(241000, '241,000 - 270,000 KES'),
(271000, '271,000 - 300,000 KES'),
(301000, '301,000 - 330,000 KES'),
(331000, '331,000 - 360,000 KES'),
(361000, '361,000 - 390,000 KES'),
(391000, '391,000 - 420,000 KES'),
(421000, '421,000 - 450,000 KES'),
(451000, '451,000 - 480,000 KES'),
(481000, '481,000 - 510,000 KES'),
(511000, '511,000 - 540,000 KES'),
(541000, '541,000 - 570,000 KES'),
(571000, '571,000 - 600,000 KES'),
(601000, '601,000 - 630,000 KES'),
(631000, '631,000 - 660,000 KES'),
(661000, '661,000 - 690,000 KES'),
(691000, '691,000 - 720,000 KES'),
(721000, '721,000 - 750,000 KES'),
(751000, '751,000 - 780,000 KES'),
(781000, '781,000 - 810,000 KES'),
(811000, '811,000 - 840,000 KES'),
(841000, '841,000 - 870,000 KES'),
(871000, '871,000 - 900,000 KES'),
(901000, '901,000 - 930,000 KES'),
(931000, '931,000 - 960,000 KES'),
(961000, '961,000 - 990,000 KES'),
(991000, '991,000 - 1,000,000 KES'),

)

COUNTY_CHOICES = (
('Baringo', 'Baringo'),
('Bomet', 'Bomet'),
('Bungoma', 'Bungoma'),
('Busia', 'Busia'),
('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
('Embu', 'Embu'),
('Garissa', 'Garissa'),
('Homa Bay', 'Homa Bay'),
('Isiolo', 'Isiolo'),
('Kajiado', 'Kajiado'),
('Kakamega', 'Kakamega'),
('Kericho', 'Kericho'),
('Kiambu', 'Kiambu'),
('Kilifi', 'Kilifi'),
('Kirinyaga', 'Kirinyaga'),
('Kisii', 'Kisii'),
('Kisumu', 'Kisumu'),
('Kitui', 'Kitui'),
('Kwale', 'Kwale'),
('Laikipia', 'Laikipia'),
('Lamu', 'Lamu'),
('Machakos', 'Machakos'),
('Makueni', 'Makueni'),
('Mandera', 'Mandera'),
('Meru', 'Meru'),
('Migori', 'Migori'),
('Marsabit', 'Marsabit'),
('Mombasa', 'Mombasa'),
('Muranga', 'Muranga'),
('Nairobi', 'Nairobi'),
('Nakuru', 'Nakuru'),
('Nandi', 'Nandi'),
('Narok', 'Narok'),
('Nyamira', 'Nyamira'),
('Nyandarua', 'Nyandarua'),
('Nyeri', 'Nyeri'),
('Samburu', 'Samburu'),
('Siaya', 'Siaya'),
('Taita-Taveta', 'Taita-Taveta'),
('Tana River', 'Tana River'),
('Tharaka-Nithi', 'Tharaka-Nithi'),
('Trans Nzoia', 'Trans Nzoia'),
('Turkana', 'Turkana'),
('Uasin Gishu', 'Uasin Gishu'),
('Vihiga', 'Vihiga'),
('Wajir', 'Wajir'),
('West Pokot', 'West Pokot'),
)


JOB_TYPE = (
    ('Full Time', "Full time"),
    ('Part Time', "Part time"),
    ('Internship', "Internship"),
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
    location = models.CharField(max_length=30, choices=COUNTY_CHOICES, default='Nairobi')
    job_type = models.CharField(choices=JOB_TYPE, max_length=100)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.IntegerField(choices=SALARY_RANGE_CHOICES, default='Confidential')
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

