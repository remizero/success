# Python Libraries / Librerías Python
from flask           import Flask
from flask_principal import Principal

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Preconditions / Precondiciones


class SuccessAclExtension ( SuccessExtension ) :
  """
  ACL (Access Control List) extension for the Success framework.

  Integrates Flask-Principal for role-based access control
  and permission management.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the ACL extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = Principal ()


  def policyDefaults ( self ) -> dict :
    """
    Get default policy settings for ACL.

    Returns:
      dict: Dictionary with default ACL policy settings.
    """
    return {
      "require_acl"       : False,
      "roles_any"         : [],
      "permissions_all"   : []
    }
