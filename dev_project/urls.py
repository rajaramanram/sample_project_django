"""four_table_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from four_table_app import views
from django.conf.urls import url

urlpatterns = [
    path('store/', views.store_usage_log, name="store_usage_log"),
    path('store_log/', views.store_log_entry, name="store_log_entry"),
    #path('change_log/', views.change_log_entry, name="change_log_entry"),
    url(r'^change_log/(?P<pk>\d+)$', views.change_log_entry, name="change_log_entry"),
    path('change_usage_log/', views.change_usage_log, name="change_usage_log"),
    path('admin/', admin.site.urls)

]
