# Python Libraries / Librerías Python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


# Application Libraries / Librerías de la Aplicación
from kernel import Extension


# Preconditions / Precondiciones


class Database ( Extension ) :

  def __init__ ( self ) -> None :
    super ().__init__ ()
    self.extension = SQLAlchemy ()

  def config ( self ) -> None :
    pass

  def metadata ( self ) -> MetaData :
    metadata = MetaData ()
    metadata.reflect ( self.extension.engine )
    return metadata

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    self.extension.init_app ( _app )

  def userConfig ( self, **kwargs ) -> None :
    pass
