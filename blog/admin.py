from django.contrib import admin
from blog.models import Blog, Contact, About

admin.site.site_header = "Factual Vibes"
admin.site.site_title = "Factual Vibes"

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css",)
        }
        
        js = ("js/blog.js",)

class AboutAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/about.js",)



admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
admin.site.register(About, AboutAdmin)