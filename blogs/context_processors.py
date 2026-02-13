from .models import Category, About


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


# def get_About(request):
#     about = About.objects.first()
#     print(about)
#     return dict(about=about)
