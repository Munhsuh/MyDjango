from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Food, TourPackage, Nomad

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)  # the TextField/CharField you want rich
    list_display = ('title', 'created_at')
    fields = ('title', 'content', 'image', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Food)
class FoodAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)

@admin.register(TourPackage)
class TourPackageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'created_at')

@admin.register(Nomad)
class NomadAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)

