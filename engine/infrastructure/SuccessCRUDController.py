# Python Libraries / Librerías Python
from typing import Any, Dict, List

# Success Libraries / Librerías Success
from success.engine.infrastructure.SuccessModelController import SuccessModelController
from success.engine.models.SuccessModel                   import SuccessModel

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessCRUDController ( SuccessModelController ) :
  """
  Implementación concreta del contrato SuccessModelController.
  Implementa operaciones estándar CRUD y de consulta usando un SuccessModel asociado.
  """

  def create(self, payload: Dict[str, Any]) -> Dict[str, Any]:
    instance = self._model.create_from_payload(payload)
    return instance.to_dict()


  def read(self, payload: Dict[str, Any]) -> Dict[str, Any]:
    # Alias de get (útil para REST o CLI)
    return self.get(payload)


  def get(self, payload: Dict[str, Any]) -> Dict[str, Any]:
    id = payload.get("id")
    if not id:
        raise ValueError("El campo 'id' es requerido en 'get'")
    instance = self._model.get_by_id(id)
    return instance.to_dict()


  def update(self, payload: Dict[str, Any]) -> Dict[str, Any]:
    id = payload.get("id")
    if not id:
        raise ValueError("El campo 'id' es requerido en 'update'")
    instance = self._model.get_by_id(id)
    instance.update_from_payload(payload)
    return instance.to_dict()


  def delete(self, payload: Dict[str, Any]) -> Dict[str, Any]:
    id = payload.get("id")
    if not id:
        raise ValueError("El campo 'id' es requerido en 'delete'")
    instance = self._model.get_by_id(id)
    instance.delete()
    return {"status": "deleted", "id": id}


  def listing(self, payload: Dict[str, Any]) -> Dict[str, Any]:
    items = self._model.list_all()
    return {"items": [item.to_dict() for item in items]}


  def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
    # Supone que el modelo implementa un método `query(...)`
    items = self._model.query(payload)
    return {"items": [item.to_dict() for item in items]}
