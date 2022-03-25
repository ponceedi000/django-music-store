from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
      
    if obj.seller is None:
      return True

    return obj.seller == request.user
