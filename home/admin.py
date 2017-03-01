from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.HomePage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ('biography',)


@admin.register(models.Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('short_descr', 'long_descr')


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')


@admin.register(models.Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'short_descr')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')
