"""
URL configuration for sorveteria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from configa.views import home, novo_produto, update, delete

urlpatterns = [
    path("admin/", admin.site.urls, name='url_admin'),
    path("", home, name='url_home'),
    path("create/", novo_produto, name='url_create'),
    path("update/<int:pk>/", update, name='url_update'),
    path("delete/<int:pk>/", delete, name='url_delete')
]
