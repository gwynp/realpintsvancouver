from django.contrib import admin

# Register your models here.
import core.models as coremodels
admin.site.register(coremodels.Location)
admin.site.register(coremodels.Review)