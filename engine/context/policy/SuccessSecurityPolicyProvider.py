# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.engine.context.policy.SuccessPolicyProvider import SuccessPolicyProvider

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessSecurityPolicyProvider ( SuccessPolicyProvider ) :
  """
  Security policy provider.

  Evaluates security policies by checking if the security extension
  is available and properly configured.
  """


  def supports ( self, spec : dict, context : dict ) -> bool :
    """
    Check if this provider supports the security policy specification.

    Args:
      spec: Policy specification dictionary.
      context: Evaluation context dictionary.

    Returns:
      bool: True if spec contains 'require_security'.
    """
    if not isinstance ( spec, dict ) :
      return False
    return bool ( spec.get ( "require_security" ) )


  def evaluate ( self, spec : dict, context : dict ) -> dict :
    """
    Evaluate the security policy against the context.

    Args:
      spec: Policy specification dictionary.
      context: Evaluation context dictionary.

    Returns:
      dict: Allow result if security extension is available, deny result otherwise.
    """
    extension = self._getExtension ( context, "security" )
    if extension is None :
      return self.deny ( 500, "Extensión Security no disponible.", "SECURITY_EXTENSION_MISSING", "security" )

    return self.allow ()


  def _getExtension ( self, context : dict, key : str ) :
    """
    Get an extension from the context.

    Args:
      context: Evaluation context dictionary.
      key: Extension key to retrieve.

    Returns:
      The extension instance or None if not found.
    """
    if not isinstance ( context, dict ) :
      return None
    extensions = context.get ( "extensions", {} )
    if not isinstance ( extensions, dict ) :
      return None
    return extensions.get ( key )
