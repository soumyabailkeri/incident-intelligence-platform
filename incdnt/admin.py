from django.contrib import admin

# Register your models here.

from .models import (
    Category,
    Incident,
    UserProfile
)

admin.site.register(Category)
admin.site.register(Incident)
admin.site.register(UserProfile)