from django.shortcuts import render

from blogs.models import Blog, About, SocialLink


def home(request):

    featured_posts = Blog.objects.filter(is_featured=True, status="Published")
    posts = Blog.objects.filter(is_featured=False, status="Published")
    about = About.objects.first()
    # social_links = SocialLink.objects.all()
    context = {
        "featured_posts": featured_posts,
        "posts": posts,
        "about": about,
        # "social_links": social_links,
    }
    return render(request, "home.html", context)
