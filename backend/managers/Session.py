# Python Libraries / Librerías Python
from flask import (
  request,
  session
)
from typing import Any


# Application Libraries / Librerías de la Aplicación
from kernel import Debug


# Preconditions / Precondiciones


class Session () :

  @staticmethod
  def create ( user, token : str = None ) -> None :
    Debug.log ( type ( session ) )
    Debug.log ( session )
    session [ 'id' ] = user.id
    session [ 'ipAddress' ] = request.remote_addr
    if ( token is not None ) :
      session [ 'token' ] = token
    #session [ 'group_id' ] = user.group_id
    #session [ 'role_id' ] = user.role_id
    Debug.log ( session )
    Debug.log ( session.sid )

  @staticmethod
  def destroy () -> None :
    session.clear ()

  @staticmethod
  def get ( key : str ) -> Any :
    return session.get ( key )

  @staticmethod
  def remove ( key : str ) -> None :
    session.pop ( key, None )
    session.modified = True

  @staticmethod
  def set ( key : str, value : Any ) -> None :
    session [ key ] = value
    session.modified = True

  @staticmethod
  def sid () -> str :
    return session.sid
