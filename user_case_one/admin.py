from django.contrib import admin
#from django.apps import apps
from .models import usage_log,log_entry


# Register your models here.
admin.site.register(usage_log)
admin.site.register(log_entry)
#models = apps.get_models()

#for i in models:
    #admin.site.register(i)