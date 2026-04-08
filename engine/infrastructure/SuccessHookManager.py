# Python Libraries / Librerías Python
from pathlib import Path
import json
import importlib
import inspect

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessClass          import SuccessClass
from success.common.tools.SuccessClasses       import SuccessClasses
from success.common.tools.SuccessFile          import SuccessFile
from success.core.SuccessContext               import SuccessContext
from success.engine.infrastructure.SuccessHook import SuccessHook

# Preconditions / Precondiciones


class SuccessHookManager ( SuccessClass ) :

  _data   : dict          = None
  _hooks  : dict          = []


  def __init__ ( self ) :
    super ().__init__ ()
    self._hooks  = []
    self._data   = SuccessFile.loadAppJson ( "hooks.json" )


  def execute ( self, when : str, action : str, **kwargs ) -> None :
    self._logger.log ( f"Ejecutando hooks (when={when}, action={action})...", "INFO" )

    executed = False

    for hook in self._hooks :
      if hook [ "when" ] == when and hook [ "action" ] == action :
        callback = hook [ "callback" ]
        payload = hook [ "payload" ]

        try :
          sig = inspect.signature ( callback )
          if len ( sig.parameters ) == 0 :
            callback ()

          elif len ( sig.parameters ) == 1 :
            callback ( payload )

          else :
            callback ( payload, **kwargs )

          executed = True

          self._logger.log ( f"Hook ejecutado exitosamente (name={hook [ 'name' ]}).", "INFO" )

        except Exception as e :
          self._logger.log ( f"Error ejecutando hook (name={hook [ 'name' ]}): {e}", "ERROR" )

    if not executed :
      self._logger.log ( f"No se encontraron hooks coincidentes (when={when}, action={action}).", "WARNING" )


  def register ( self ) :
    if not self._data :
      self._logger.log ( f"No se registraron Hooks para la aplicación {SuccessContext ().getCurrentAppName ()}.", "WARNING" )
      return

    for idx, hook in enumerate ( self._data ) :
      name     = hook.get ( "name", f"unnamed_hook_{idx}" )
      callback = hook.get ( "callback" )
      when     = hook.get ( "when" )
      action   = hook.get ( "action" )
      payload  = hook.get ( "payload", {} )

      if not isinstance ( callback, str ) :
        self._logger.log ( f"[{name}] El 'callback' debe ser una cadena tipo 'Modulo.Clase.metodo'.", "ERROR" )
        continue

      if when not in [ "before", "after" ] :
        self._logger.log ( f"[{name}] Valor de 'when' inválido: '{when}'. Debe ser 'before' o 'after'.", "ERROR" )
        continue

      if not action :
        self._logger.log ( f"[{name}] Se requiere un 'action' para categorizar el hook.", "ERROR" )
        continue

      try :

        method = self.resolveCallback ( callback )

      except Exception as e :
        self._logger.log ( f"[{name}] Error al resolver el callback '{callback}': {e}", "ERROR" )
        continue

      self._hooks.append (
        {
          "name"     : name,
          "callback" : method,
          "when"     : when,
          "action"   : action,
          "payload"  : payload or {}
        }
      )

      self._logger.log ( f"Hook registrado correctamente (name={name}, when={when}, action={action}).", "INFO" )


  def resolveCallback ( self, callback : str ) -> callable :
    try :
      parts = callback.split ( "." )
      if len ( parts ) < 3 :
        raise ValueError ( f"Callback '{callback}' debe tener formato completo: paquete.Clase.metodo" )

      *moduleParts, className, methodName = parts

      module = SuccessClasses.getModule ( "infrastructure", moduleParts, className )
      klass  = SuccessClasses.getClassFromModule ( module, className )

      if not issubclass ( klass, SuccessHook ) :
        raise TypeError ( f"La clase '{className}' no hereda de SuccessHook." )

      method = SuccessClasses.getMethodFromClass ( klass (), methodName )

      if not callable ( method ) :
        raise TypeError ( f"El método '{methodName}' no es invocable." )

      return method

    except Exception as e :
      raise RuntimeError ( f"Error resolviendo callback '{callback}': {e}" )
