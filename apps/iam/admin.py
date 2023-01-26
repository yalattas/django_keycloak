from django.contrib import admin

from .models import User, SessionLog


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'id',
        # 'password',
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'first_name',
        'last_name',
        'is_blocked',
        'is_email_verified',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'is_blocked',
    )
    raw_id_fields = ('groups', 'user_permissions')

@admin.register(SessionLog)
class SessionLogAdmin(admin.ModelAdmin):
    list_display = (
        'session_id',
        'client_id',
        'created_at',
        'modified_at',
        'is_deleted',
    )
    readonly_fields = [
        'session_id',
        'client_id',
    ]
    list_filter = ('client_id', 'created_at', 'modified_at', 'is_deleted')
    date_hierarchy = 'created_at'