"""ClubWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import ClubWebsite.views as clubViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', clubViews.home, name='home'),
    path('projects/', clubViews.home, name='projects'),
    path('blog/', clubViews.home, name='blog'),
    path('about/', clubViews.about, name='about'),
    path('team_members/', clubViews.team_members, name='team_members'),
    path('sponsor/', clubViews.sponsor, name='sponsor'),
    path('join_us/', clubViews.home, name='join_us'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
