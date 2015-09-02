from django.contrib import admin
from core.models import UserProfile

# Register your models here.
import core.models as coremodels
admin.site.register(coremodels.Location)
admin.site.register(coremodels.Review)
admin.site.register(UserProfile)