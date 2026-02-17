from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'role', 'is_staff', 'is_active', 'username']  # ← username тоже!
    list_filter = ['is_staff', 'is_superuser', 'role', 'is_active']
    search_fields = ['email', 'full_name', 'username']
    readonly_fields = ['username']  # username генерируется из email
