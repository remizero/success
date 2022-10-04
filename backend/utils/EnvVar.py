# Python Libraries / Librerías Python
import ast
import os


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones


class EnvVar () :

  @staticmethod
  def get ( envVar : str ) -> str :
    return os.environ.get ( envVar )

  @staticmethod
  def getCorsResources () -> dict :
    resource = '{ '
    corsResources = EnvVar.toList ( 'CORS_RESOURCES_APP_RESOURCES' )
    corsOrigins = EnvVar.toList ( 'CORS_RESOURCES_APP_ORIGINS' )
    corsMethods = EnvVar.toList ( 'CORS_RESOURCES_APP_METHODS' )
    corsAllowed = EnvVar.toList ( 'CORS_RESOURCES_APP_ALLOW_HEADERS' )
    corsExposes = EnvVar.toList ( 'CORS_RESOURCES_APP_EXPOSE_HEADERS' )
    for i in range ( len ( corsResources ) ) :
      resource += corsResources [ i ] + ' : { '
      resource += '\'origins\' : ' + EnvVar.listToString ( corsOrigins, i ) + ', '
      resource += '\'methods\' : ' + EnvVar.listToString ( corsMethods, i ) + ', '
      resource += '\'allow_headers\' : ' + EnvVar.listToString ( corsAllowed, i ) + ', '
      resource += '\'expose_headers\' : ' + EnvVar.listToString ( corsExposes, i )
      resource += ' }, '
    resource = resource [ : -2 ]
    resource += ' }'
    return EnvVar.toResource ( resource )

  @staticmethod
  def isEmpty ( envVar : str ) -> bool :
    return ( EnvVar.get ( envVar ) == '' )

  @staticmethod
  def isTrue ( envVar : str ) -> bool :
    return ( ( EnvVar.get ( envVar ) == 'True' ) or ( EnvVar.get ( envVar ) == 'true' ) )

  @staticmethod
  def listToString ( envVarList : list, index : int = 0 ) -> str :
    return envVarList [ index ].__repr__ ()

  @staticmethod
  def toList ( envVar : str ) -> list :
    toReturn = list ()
    if ( EnvVar.wellFormedList ( envVar ) ) :
      toReturn = os.environ.get ( envVar ).strip ( ' ][ ' ).split ( ', ' )
    else :
      toReturn = ast.literal_eval ( EnvVar.get ( envVar ) )
    return toReturn

  @staticmethod
  def toResource ( resource : str ) -> dict :
    return ast.literal_eval ( resource )

  @staticmethod
  def wellFormedList ( envVar : str ) -> bool :
    string = EnvVar.get ( envVar )
    return ( 'r\'' in string ) and ( '[' in string ) and ( ']' in string )
