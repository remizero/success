# Python Libraries / Librerías Python
from abc import (
  ABC,
  abstractmethod
)
from flask import (
  request,
  session
)
from typing import Any


# Application Libraries / Librerías de la Aplicación
from . import (
  Debug,
  Logger
)


# Preconditions / Precondiciones


# TODO ESTA CLASE BASE ES UN INTENTO POR INCLUIR TODOS LOS ASPECTOS REPETITIVOS DE TODAS LAS CLASES DEL SISTEMA
class BaseClass ( ABC ) :

  @abstractmethod
  def __init__ ( self ) -> None :
    pass
