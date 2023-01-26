from rest_framework.permissions import BasePermission

class CustomerProfileAccess(BasePermission):
    message = ('User has no access.')

    def has_permission(self, request, view):
        user = request.user
        try:
            if user.groups.filter(name='CustomerGroup').exists():
                return True
            return False
        # except CorporateEmployeeProfile.DoesNotExist:
        except Exception as e:
            return False
