from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
  """Allow user to edit their own profile

  Args:
      permissions (_type_): _description_
  """
  
  def has_object_permission(self, request, view, obj):
    """CHeck user is trying to edit own profile

    Args:
        request (_type_): _description_
        view (_type_): _description_
        obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.id == request.user.id
  
class UpdateOwnStatus(permissions.BasePermission):
  """Allow users to update their own status

  Args:
      permissions (_type_): _description_
  """
  
  def has_object_permission(self, request, view, obj):
    """Check the user is trying to update their own status

    Args:
        request (_type_): _description_
        view (_type_): _description_
        obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.user_profile.id == request.user.id