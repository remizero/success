# Python Libraries / Librerías Python
from flask import Flask


# Application Libraries / Librerías de la Aplicación
from kernel import Extension


# Preconditions / Precondiciones


class Routes ( Extension ) :

  def __init__ ( self ) -> None :
    super ().__init__ ()

  def config ( self ) -> None :
    pass

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    pass

  def userConfig ( self, **kwargs ) -> None :
    pass
