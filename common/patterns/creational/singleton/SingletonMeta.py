# Python Libraries / Librerías Python
from threading import Lock

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SingletonMeta ( type ) :

  _instances        = {}
  _lock      : Lock = Lock ()


  def __call__ ( cls, *args, **kwargs ) :
    with cls._lock :
      if cls not in cls._instances :
        instance = super ().__call__ ( *args, **kwargs )
        cls._instances [ key ] = instance

    return cls._instances [ key ]
