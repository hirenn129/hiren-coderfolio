from django.shortcuts import render


def about_page(request):
    return render(request, "about.html")


def blog_details(request):
    return render(request, "blog_details.html")


def blog(request):
    return render(request, "blog.html")


def contect(request):
    return render(request, "contact.html")


def elements(request):
    return render(request, "elements.html")


def error404(request):
    return render(request, "404notfound.html")


def index(request):
    return render(request, "home.html")


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
