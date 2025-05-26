from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_desc = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)

    CATEGORY_CHOICES = [
        ('fact', 'Fact'),
        ('scripture', 'Scripture'),
        ('sports', 'Sports'),
        ('other', 'Other'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

    image = models.ImageField(upload_to="blog_images/", null=True, blank=True)

    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return "About Page"


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    time = models.DateTimeField(auto_now=True)
