from django.shortcuts import render

from blogs.models import Blog, Category

# Create your views here.


def dashboard(request):
    total_cat = Category.objects.all().count()
    total_post = Blog.objects.all().count()
    context = {
        "total_categories": total_cat,
        "total_post": total_post,
    }
    return render(request, "dashboards/dashboard.html", context)
