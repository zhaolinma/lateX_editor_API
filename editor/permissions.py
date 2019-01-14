from rest_framework import permissions
'''
class isOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is 'OPTIONS':#Allow options method for all
            return True
        if request.method in permissions.SAFE_METHODS \
        and request.user.is_authenticated():# read only for login user
            return True

        return obj.author == request.user# modified only by creator
'''
class isOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True 
        return obj.author == request.username
