from django.contrib import admin

from .models import *

# Khamza
# Alhamdulillah

class SunnatHadithAdmin(admin.StackedInline):
    model = SunnatHadith


@admin.register(Sunnat)
class SunnatAdmin(admin.ModelAdmin):
    inlines = [SunnatHadithAdmin]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(SunnatCategory)
class SunnatCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}