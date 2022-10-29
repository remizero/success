# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Exception import Exception

# Preconditions / Precondiciones


class OutputException ( Exception ) :

  def __init__ ( self ) :
    self.message = "No se ha definido un tipo de salida valida para la respuesta a ser enviada."
    