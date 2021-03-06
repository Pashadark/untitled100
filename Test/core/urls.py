"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# fmt: off
# (Skip Black formatting in this section)
urlpatterns = [
    # NOTE: change the URL for Admin, for added security.
    # See #2 here: https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="homepage.html"), name="homepage"),
    path("contact/", TemplateView.as_view(template_name="contact.html"), name="contact"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("calculator/", TemplateView.as_view(template_name="calculator.html"), name="calculator"),
    path("news/", TemplateView.as_view(template_name="news.html"), name="news"),
    url(r'^emoji/', include('emoji.urls')),

]
# fmt: on

if settings.DEBUG:
    # Serve media files in development server.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
