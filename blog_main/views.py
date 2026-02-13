from django.shortcuts import render

from blogs.models import Blog, About


def home(request):

    featured_posts = Blog.objects.filter(is_featured=True, status="Published")
    posts = Blog.objects.filter(is_featured=False, status="Published")
    about = About.objects.first()
    context = {"featured_posts": featured_posts, "posts": posts, "about": about}
    return render(request, "home.html", context)
