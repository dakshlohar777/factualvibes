from django.shortcuts import render, HttpResponse
from blog.models import Blog, Contact, About
import math

def home(request):
    top_facts = Blog.objects.filter(category='fact')[:3]
    top_scriptures = Blog.objects.filter(category='scripture')[:3]
    top_scriptures = Blog.objects.filter(category='scripture')[:3]

    context = {
        'top_facts': top_facts,
        'top_scriptures': top_scriptures
    }
    return render(request, 'index.html', context)

def base(request):
    return render(request, 'base.html')

def blog(request):
    no_of_posts = 7
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
    
    prev = page - 1 if page > 1 else None
    nxt = page + 1 if page < math.ceil(length / no_of_posts) else None
    
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'bloghome.html', context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request, 'blogpost.html', context)

def about(request):
    about_data = About.objects.first()
    context = {
        'about': about_data,
        'title': 'About Us'
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()
    return render(request, 'contact.html')
