# Python Libraries / Librerías Python
from contextvars import ContextVar
from typing      import Optional

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class RequestContext () :

  __appId : ContextVar [ Optional [ str ] ] = ContextVar ( "app_id", default = None )
  __requestId : ContextVar [ Optional [ str ] ] = ContextVar ( "request_id", default = None )


  @classmethod
  def clear ( cls ) -> None :
    cls.__appId.set ( None )
    cls.__requestId.set ( None )


  @staticmethod
  def _detectAppId () -> str :
    # Detecta dinámicamente el nombre de la apps a partir de la ruta
    try :
      return os.path.basename ( os.path.dirname ( os.path.abspath ( __file__ ) ) )
      
    except Exception :
      return "unknown"


  @classmethod
  def getAppId ( cls ) -> Optional [ str ] :
    return cls.__appId.get ()


  @classmethod
  def getRequestId ( cls ) -> Optional [ str ] :
    return cls.__requestId.get ()


  @classmethod
  def setAppId ( cls, app_id : Optional [ str ] = None ) -> None :
    if app_id :
      cls.__appId.set ( app_id )

    else :
      # Fallback automático si no se pasa app_id manualmente
      dynamicAppId = cls._detectAppId ()
      cls.__appId.set ( dynamicAppId )


  @classmethod
  def setRequestId ( cls, request_id : str ) -> None :
    cls.__requestId.set ( request_id )
