from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField



Author = get_user_model()



# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=25)

    class Meta:
     verbose_name='category'
     verbose_name_plural='categories'


    def __str__(self):
        return self.title
  


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='Author', on_delete=models.CASCADE,null=False) 
    slug=models.SlugField(max_length=200,unique=True)
    # header_image= models.ImageField(null=True, blank=True,upload_to="blogs")
    header_image= ResizedImageField(size=[400, 400],upload_to="blogs")
    # body=models.TextField()
    body = RichTextUploadingField() # CKEditor Rich Text Field

    date_added = models.DateTimeField(auto_now_add=True)
    comment_count=models.IntegerField(default=0)
    category=models.ManyToManyField(Category)

    class Meta:
        ordering= ['-date_added']
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})





class Comment(models.Model):
    post =models.ForeignKey(Blog, related_name="comments" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email=models.EmailField(null=False)
    body=models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return  '%s - %s' % (self.post.title, self.name)