# Python Libraries / Librerías Python
from typing import Any, Dict, List

# Success Libraries / Librerías Success
from success.engine.infrastructure.SuccessController import SuccessController
from success.engine.models.SuccessModel              import SuccessModel

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessModelController ( SuccessController ) :
  """
  Contrato base para todos los controladores del ecosistema Success.

  - Todos los métodos reciben un `payload: dict` que ya ha sido
    normalizado por la capa Input.
  - Cada método debe retornar un `dict` compatible con Output.
  - La ejecución puede ser dinámica vía `execute(...)`.
  - Se permite hook previo por método (`before_method`).
  """

  _model : Type [ SuccessModel ] = None


  def __init__ ( self ) :
    if not self._model :
      raise ValueError ( f"{self.__class__.__name__} debe definir un atributo '_model'" )


  # Métodos CRUD convencionales (optativos de implementar)
  def create ( self, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    raise NotImplementedError ( "Método 'create' no implementado." )


  def read ( self, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    raise NotImplementedError ( "Método 'read' no implementado." )


  def update ( self, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    raise NotImplementedError ( "Método 'update' no implementado." )


  def delete ( self, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    raise NotImplementedError ( "Método 'delete' no implementado." )


  def get ( self, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    raise NotImplementedError ( "Método 'get' no implementado." )


  def listing ( self, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    raise NotImplementedError ( "Método 'listing' no implementado." )


  def query ( self, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    raise NotImplementedError ( "Método 'query' no implementado." )
