from rest_framework.permissions import BasePermission
from .models import Permission


class CustomRBACPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated or not user.is_active:
            return False

        if user.is_superuser:
            return True

        if hasattr(view, 'admin_resource') and user.role.name == 'admin':
            return True

        resource = getattr(view, 'resource', None)
        if not resource:
            return True

        action_map = {
            'GET': 'view', 'HEAD': 'view', 'OPTIONS': 'view',
            'POST': 'create',
            'PUT': 'update', 'PATCH': 'update',
            'DELETE': 'delete'
        }
        action = action_map.get(request.method, 'view')

        return Permission.objects.filter(
            role=user.role,
            resource__name=resource,
            action__name=action
        ).exists()
