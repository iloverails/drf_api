from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 1:
            return True

        return False


class IsTenant(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 4:
            return True

        return False


class IsLandlord(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 3:
            return True

        return False


class IsReviewer(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 2:
            return True

        return False
