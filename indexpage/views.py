from django.shortcuts import render
from indexpage.models import User


def about_page(request):
    return render(request, "about.html")


def blog_details(request):
    return render(request, "blog_details.html")


def blog(request):
    return render(request, "blog.html")


def contect(request):
    try:
        if request.method == "POST":
            discription = request.POST.get("discription")
            email = request.POST.get("email")
            name = request.POST.get("name")
            subject = request.POST.get("subject")
            user_created = User(
                discription=discription, email=email, name=name, subject=subject
            )
            user_created.save()

    except Exception as e:
        print(e)

    return render(request, "contact.html")


def elements(request):
    return render(request, "elements.html")


def error404(request):
    return render(request, "404notfound.html")


def index(request):
    try:
        if request.method == "POST":
            discription = request.POST.get("discription")
            email = request.POST.get("email")
            name = request.POST.get("name")
            user_created = User(discription=discription, email=email, name=name)
            user_created.save()

    except Exception as e:
        print(e)

    return render(request, "index.html")


def main(request):
    return render(request, "main.html")


def portfolio_details(request):
    return render(request, "portfolio_details.html")


def portfolio(request):
    return render(request, "portfolio.html")


def services(request):
    return render(request, "services.html")


def resume(request):
    return render(request, "resume.html")
