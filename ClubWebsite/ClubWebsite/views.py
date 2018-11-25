from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def projects(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def team_members(request):
    return render(request, "index.html")

def sponsor(request):
    return render(request, "sponsor.html")

def join_us(request):
    return render(request, "index.html")
