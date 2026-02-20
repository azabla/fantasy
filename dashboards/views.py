from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from .forms import BlogForm, CategoryForm

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


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm(instance=category)
    context = {"form": form, "category": category}
    return render(request, "dashboards/edit_category.html", context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("categories")


def posts(request):
    posts = Blog.objects.all()
    form = BlogForm()
    context = {"form": form, "posts": posts}
    return render(request, "dashboards/posts.html", context)


def add_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        # post = form.cleaned_data('author')
        if form.is_valid():
            post = form.save(commit=False)  # temporarly saving the form
            post.author = request.user
            post.save()
            title = form.cleaned_data["title"] + "-" + str(post.id)
            post.slug = slugify(title)
            post.save()
            return redirect("posts")
        else:
            print(form.errors)
    form = BlogForm()
    context = {"form": form}
    return render(request, "dashboards/add_post.html", context)


def edit_post(request, pk):

    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data["title"] + "-" + str(post.id)
            post.slug = slugify(title)
            post.save()
            return redirect("posts")

    form = BlogForm(instance=blog)
    context = {"form": form, "blog": blog}

    return render(request, "dashboards/edit_post.html", context)


def delete_post(reqeust, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect("posts")
