# Python Libraries / Librerías Python
from abc    import ABC
from abc    import abstractmethod
from flask  import request
from flask  import session
from typing import Any


# Application Libraries / Librerías de la Aplicación
from kernel import Debug
from kernel import Logger


# Preconditions / Precondiciones


# TODO ESTA CLASE BASE ES UN INTENTO POR INCLUIR TODOS LOS ASPECTOS REPETITIVOS DE TODAS LAS CLASES DEL SISTEMA
class BaseClass ( ABC ) :

  logger : Logger = None

  @abstractmethod
  def __init__ ( self ) -> None :
    self.logger = Logger ( __name__ )
    pass
