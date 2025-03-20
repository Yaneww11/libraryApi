from rest_framework import permissions


class IsBookOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        authors_names = obj.author.values_list('name', flat=True)
        return request.user.username in authors_names