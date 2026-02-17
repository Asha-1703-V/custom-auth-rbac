from django.contrib import admin
from .models import Role, Resource, Action, Permission

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = ['name']

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['role', 'resource', 'action']
    list_filter = ['role', 'resource']
