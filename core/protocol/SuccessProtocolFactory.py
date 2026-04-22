# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.core.protocol.SuccessProtocolAdapter        import SuccessProtocolAdapter
from success.core.protocol.SuccessDefaultProtocolAdapter import SuccessDefaultProtocolAdapter
from success.core.protocol.SuccessRestProtocolAdapter    import SuccessRestProtocolAdapter
from success.core.protocol.SuccessViewProtocolAdapter    import SuccessViewProtocolAdapter
from success.core.SuccessBuildContext                    import SuccessBuildContext

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessProtocolFactory:
  """
  Protocol adapter factory for endpoints.

  Selects and creates the appropriate protocol adapter according to the
  endpoint type (view, restful, default).

  Usage:
      adapter = SuccessProtocolFactory.getProtocolAdapter('view')
      adapter.register(ctx, blueprint, options)
  """


  @staticmethod
  def getProtocolAdapter ( protocol : str ) -> SuccessProtocolAdapter :
    """
    Get a protocol adapter instance according to the requested type.

    Args:
      protocol: Protocol type ('view', 'restful', or any other for default).

    Returns:
      SuccessProtocolAdapter: Instance of the corresponding adapter.

    Example:
      view_adapter = SuccessProtocolFactory.getProtocolAdapter('view')
      rest_adapter = SuccessProtocolFactory.getProtocolAdapter('restful')
      default_adapter = SuccessProtocolFactory.getProtocolAdapter('custom')
    """
    if protocol.lower () == "view" :
      return SuccessViewProtocolAdapter ()

    elif protocol.lower () == "restful" :
      return SuccessRestProtocolAdapter ()
      
    else :
      return SuccessDefaultProtocolAdapter ()
