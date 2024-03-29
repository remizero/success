# Python Libraries / Librerías Python
from datetime           import datetime
from datetime           import timedelta
from flask              import current_app
from flask              import Flask
from flask              import json
from flask              import Response
from flask              import jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import decode_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import set_refresh_cookies
from flask_jwt_extended import unset_jwt_cookies
from http               import HTTPStatus
from redis              import StrictRedis


# Application Libraries / Librerías de la Aplicación
from exceptions                 import RevokeJwtException
from kernel.abstracts           import Extension
from kernel.abstracts.Extension import EnvVar
from kernel                     import Debug
from kernel                     import Logger
# from app.models       import TokenBlacklist
# from app.models       import User
from utils                      import Datetime
from utils                      import Http


# Preconditions / Precondiciones
jwt_redis_blocklist = None


class Jwt ( Extension ) :

  def __init__ ( self ) -> None :
    super ().__init__ ()
    self.extension = JWTManager ()

  def config ( self ) -> None :
    pass

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    self.extension.init_app ( _app )
    with _app.app_context () :
      jwt_redis_blocklist = StrictRedis (
        host              = current_app.config [ 'REDIS_HOST' ],
        port              = current_app.config [ 'REDIS_PORT' ],
        db                = current_app.config [ 'REDIS_DB' ],
        decode_responses  = current_app.config [ 'REDIS_DECODE_RESPONSES' ]
      )

  def userConfig ( self, **kwargs ) -> None :
    pass

  @staticmethod
  def create ( response : Response ) -> tuple ( [ Response, str ] ) :
    responseAux = response.get_json ()
    access_token = ''
    refresh_token = ''
    if ( EnvVar.isTrue ( 'SUCCESS_OUTPUT_MODEL' ) ) :
      access_token = create_access_token ( identity = responseAux [ 'data' ] [ 0 ] [ 'username' ] )
      refresh_token = create_refresh_token ( identity = responseAux [ 'data' ] [ 0 ] [ 'username' ] )
      responseAux [ 'data' ] [ 0 ] [ 'token' ] = access_token
    else :
      access_token = create_access_token ( identity = responseAux [ 'username' ] )
      refresh_token = create_refresh_token ( identity = responseAux [ 'username' ] )
      responseAux [ 'token' ] = access_token
    response.data = json.dumps ( responseAux )
    set_access_cookies ( response, access_token )
    set_refresh_cookies ( response, refresh_token )
    return tuple ( [ response, access_token ] )

  # Callback function to check if a JWT exists in the database blocklist
  #@staticmethod
  # @jwt.token_in_blocklist_loader
  # def check_if_token_revoked ( jwt_header, jwt_payload : dict ) -> bool :
  #   jti = jwt_payload [ 'jti' ]
  #   tokenBlacklist = TokenBlacklist ()
  #   token = tokenBlacklist.scalar ( jti = jti )
  #   return token is not None

  @staticmethod
  def get () :
    pass

  #@staticmethod
  #@jwt_required ( verify_type = False )
  # def revoke ( self ) :
  #   logger = Logger ( __name__ )
  #   try :
  #     token = get_jwt ()
  #     user = User ()
  #     userObj = user.findByFilters ( username = token [ 'sub' ] )
  #     tokenBlacklist = TokenBlacklist ( user_id = userObj [ 0 ].id, jti = token [ 'jti' ], type = token [ 'type' ], created_at = Datetime.getNow () )
  #     tokenBlacklist.insert ()
  #   except :
  #     self.logger.uncatchErrorException ()
  #     raise RevokeJwtException ()

  #@staticmethod
  @jwt_required ( refresh = True )
  def refresh () :
    identity = get_jwt_identity ()
    access_token = create_access_token ( identity = identity )
    response = Http.returnResponse ( { 'access_token' : access_token }, HTTPStatus.OK )
    set_access_cookies ( response, access_token )
    return response

  #@staticmethod
  #@jwt_required ()
  def refresh_expiring_jwts ( self, response ) :
    #logger = Logger ( __name__ )
    try:
      exp_timestamp = get_jwt () [ 'exp' ]
      now = Datetime.getNow ()
      target_timestamp = datetime.timestamp ( now + timedelta ( seconds = 5 ) )
      if target_timestamp > exp_timestamp:
        access_token = create_access_token ( identity = get_jwt_identity () )
        set_access_cookies ( response, access_token )
      return response
    except ( RuntimeError, KeyError ) :
      self.logger.uncatchErrorException ()
      # Case where there is not a valid JWT. Just return the original response
      return response

  # PARA EL MANEJO DEL TOKEN CON REDIS
  #@JWTManager.token_in_blocklist_loader ( JWTManager, jwt_redis_blocklist )
  #@JWTManager.token_in_blocklist_loader
  def check_if_token_is_revoked ( jwt_header, jwt_payload : dict ) -> bool :
    jti = jwt_payload [ 'jti' ]
    token_in_redis = jwt_redis_blocklist.get ( jti )
    return token_in_redis is not None

  # PARA EL MANEJO DEL TOKEN CON REDIS
  def logout ( self ) :
    jti = get_jwt () [ 'jti' ]
    jwt_redis_blocklist.set ( jti, '', ex = current_app.config [ 'JWT_ACCESS_TOKEN_EXPIRES' ])
    return jsonify ( msg = 'Access token revoked' )

  #@JWTManager.expired_token_loader
  def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None

  # @JWTManager.token_in_blocklist_loader
  # def check_if_token_in_blacklist(jwt_header, jwt_payload):
  #   return jwt_payload["jti"] in blocklist
