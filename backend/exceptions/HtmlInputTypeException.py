# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import Exception

# Preconditions / Precondiciones


class HtmlInputTypeException ( Exception ) :

  def __init__ ( self ) :
    self.message = "Modo Desarrollo activado, por lo que debe habilitar el \
      modo Debug = True, y debe deshabilitar el \
      modo Testing = False y \
      modo Staging = False"
    