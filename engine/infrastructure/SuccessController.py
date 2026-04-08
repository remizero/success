# Python Libraries / Librerías Python
from typing import Any, Dict, List, Type

# Success Libraries / Librerías Success
from success.engine.models.SuccessModel import SuccessModel

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessController () :
  """
  Contrato base para todos los controladores del ecosistema Success.

  - Todos los métodos reciben un `payload: dict` que ya ha sido
    normalizado por la capa Input.
  - Cada método debe retornar un `dict` compatible con Output.
  - La ejecución puede ser dinámica vía `execute(...)`.
  - Se permite hook previo por método (`before_method`).
  """


  # Hook: permite modificar el payload antes de ejecutar cualquier método
  def before_method ( self, method : str, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    """
    Hook que se ejecuta antes del método solicitado.
    Puede modificar o validar el payload antes de la ejecución.
    """
    return payload


  # Ejecución dinámica del método
  def execute ( self, method : str, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    """
    Ejecuta el método especificado pasando el payload como parámetro.
    Utiliza introspección para validar la existencia del método.
    """
    payload = self.before_method ( method, payload )
    if not hasattr ( self, method ) :
      raise NotImplementedError ( f"Método '{method}' no implementado en '{self.__class__.__name__}'." )
    method_ref = getattr ( self, method )
    if not callable ( method_ref ) :
      raise TypeError ( f"'{method}' no es un método ejecutable." )
    return method_ref ( payload )


  def get_model ( self ) -> Type [ SuccessModel ] :
    """Devuelve el modelo asociado, si lo hay."""
    return getattr ( self, "_model", None )


  @property
  def has_model ( self ) -> bool :
    """Indica si el controlador tiene un modelo asociado (solo útil en subclases)."""
    return hasattr ( self, "_model" ) and self._model is not None


  @property
  def methods ( self ) -> List [ str ] :
    """
    Devuelve la lista de métodos públicos disponibles en el controlador.
    Excluye los métodos heredados de SuccessController.
    """
    base_methods = dir ( SuccessController )
    return [
      m for m in dir ( self )
      if not m.startswith ( "_" )
      and callable ( getattr ( self, m ) )
      and m not in base_methods
    ]
