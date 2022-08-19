from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=225)
    title_tag=models.CharField(max_length=225)
    post_date=models.DateField(auto_now_add=True)
    body=RichTextField(blank=True,null=True)