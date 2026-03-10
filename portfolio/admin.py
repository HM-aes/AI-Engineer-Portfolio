from django.contrib import admin
from .models import Project, SecurityModel, TechTag


@admin.register(TechTag)
class TechTagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class SecurityModelInline(admin.StackedInline):
    model = SecurityModel
    can_delete = False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "security_level", "domain", "is_featured", "order")
    list_filter = ("security_level", "domain", "is_featured")
    search_fields = ("name", "tagline", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SecurityModelInline]
    filter_horizontal = ("stack",)
