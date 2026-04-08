# Python Libraries / Librerías Python
from flask  import request
from flask  import session
from typing import Any

# Application Libraries / Librerías de la Aplicación
from success.common.SuccessDebug               import SuccessDebug
from success.common.infra.logger.SuccessLogger import SuccessLogger

# Preconditions / Precondiciones


class SuccessSession () :


  @staticmethod
  def create ( user, token : str = None ) -> None :
    logger = SuccessLogger ( __name__ )
    session [ 'id' ] = user.id
    session [ 'ipAddress' ] = request.remote_addr
    if ( token is not None ) :
      session [ 'token' ] = token
    groupsUser = user.groups.filter_by ().all ()
    session [ 'group_id' ] = groupsUser [ 0 ].id
    profiles = user.profiles.filter_by ().all ()
    session [ 'profile_id' ] = profiles [ 0 ].id
    roles = user.roles.filter_by ().all ()
    session [ 'role_id' ] = roles [ 0 ].id
    session [ 'loggedin' ] = True


  @staticmethod
  def destroy () -> None :
    session.clear ()


  @staticmethod
  def exist ( key : str ) -> bool :
    return key not in session


  @staticmethod
  def isLogin () -> bool :
    return ( SuccessSession.exist ( 'loggedin' ) and SuccessSession.get ( 'loggedin' ) is not None )
    

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
