from rest_framework import permissions

class IsClientOrContractor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.client or request.user == obj.contractor
    


