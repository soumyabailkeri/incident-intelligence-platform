from rest_framework.permissions import BasePermission


class IsManagerOrAdmin(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        try:
            role = request.user.userprofile.role

            return role in [
                "manager",
                "admin"
            ]

        except Exception:
            return False