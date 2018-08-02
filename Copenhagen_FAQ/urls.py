"""learning_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'Copenhagen_FAQ'


urlpatterns = [
    path('faq/', include('faq.urls', namespace='faq')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('admin/', admin.site.urls),
    path('suggest/', views.suggestion_view, name='suggestion'),
    path('', views.home_page, name='home'),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]