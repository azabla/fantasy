from django.shortcuts import redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm

# Create your views here.


@login_required(login_url="login")
def dashboard(request):
    total_cat = Category.objects.all().count()
    total_post = Blog.objects.all().count()
    context = {
        "total_categories": total_cat,
        "total_post": total_post,
    }
    return render(request, "dashboards/dashboard.html", context)


def categories(request):
    return render(request, "dashboards/categories.html")


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm()
    context = {"form": form}
    return render(request, "dashboards/add_category.html", context)
