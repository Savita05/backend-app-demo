"""demobackends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('createuser.urls')),
     path('openapi/', get_schema_view(
        title="Demo ADAS Tool",
        description="It is an annotation tool"
    ), name='openapi-schema'),

     path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
   

]



