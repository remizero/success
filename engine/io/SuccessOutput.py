# Python Libraries / Librerías Python
from abc   import abstractmethod
from flask import flash
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

# Application Libraries / Librerías de la Aplicación
from success.common.exceptions.OutputException    import OutputException
from success.common.infra.logger.SuccessLogger    import SuccessLogger
from success.common.SuccessDebug                  import SuccessDebug
from success.common.base.SuccessClass             import SuccessClass
from success.engine.models.SuccessSchema          import SuccessSchema
from success.common.infra.config.SuccessSystemEnv import SuccessSystemEnv
from success.common.tools.SuccessEnv              import SuccessEnv
from success.common.tools.SuccessHttp             import SuccessHttp
from success.common.tools.SuccessStructs          import SuccessStructs

# Preconditions / Precondiciones


class SuccessOutput ( SuccessClass ) :

  _hasError      : bool = None
  _isLogin       : bool = None
  _output        : dict = None
  _schemaOutput  : dict = None
  _successOutput : bool = None


  def __init__ ( self, isLogin : bool = False ) -> None :
    self._isLogin       = isLogin
    self._successOutput = SuccessEnv.isTrue ( SuccessSystemEnv.get ( 'SUCCESS_OUTPUT_MODEL' ) )
    self._wants_json    = self._detectJson ()
    if ( self._successOutput ) :
      self._schemaOutput = SuccessStructs.successOutputEmptySchema ()

    else :
      self._schemaOutput = SuccessSchema ()


  def _detectJson ( self ) :
    return (
      request.is_json or
      request.accept_mimetypes [ "application/json" ] >= request.accept_mimetypes [ "text/html" ]
    )


  def data ( self, data : dict ) -> dict :
    # Ejemplo: si tienes esquema activado
    if self._successOutput :
      self.setData ( data )
      return self.output ()

    return data


  def failure ( self,
                message            = "Ocurrió un error",
                detail             = "",
                status_code        = 400,
                redir       : dict = None,
                render      : dict = None
              ) :
    full_message = message
    if detail :
      full_message += f": {detail}"

    # JSON Case / Caso JSON
    if self._wants_json :
      payload = {
        "success" : False,
        "message" : message,
        "detail"  : detail
      }
      return jsonify ( payload ), status_code

    # Caso redirección explícita
    if redir and redir.get ( "enabled" ) :
      flash ( full_message, "error" )
      return redirect ( url_for ( redir.get ( "target" ), **redir.get ( "context", {} ) ) )

    # Caso render_template con contexto
    if render and render.get ( "enabled" ) :
      html = render_template (
        render.get ( "template" ),
        **( render.get ( "context" ) or {} )
      )
      return make_response ( html, status_code, SuccessHttp.contentTypeHtml () )

    # Fallback: texto plano
    return full_message, status_code


  def output ( self ) -> dict :
    if ( self._successOutput ) :
      if ( SuccessHttp.isMethod ( 'POST' ) and not self._hasError ) :
        self.setData ( self._output )

      else :
        self._schemaOutput = self._output

      return self._schemaOutput

    elif ( self._isLogin or self._hasError ) :
      return self._output

    else :
      return self._schemaOutput.dump ( self._output )


  def setAction ( self, action : str ) -> None :
    if ( self._successOutput ) :
      self._schemaOutput [ 'action' ] = action

    else :
      raise OutputException ()


  def setData ( self, data : list ) -> None :
    if ( self._successOutput ) :
      self._schemaOutput [ 'data' ].append ( data.copy () )

    else :
      raise OutputException ()


  def setOptions ( self, attribute : str, options : list ) -> None :
    if ( self._successOutput ) :
      for model in self._schemaOutput [ 'model' ] :
        if model [ 'name' ] == attribute :
          model [ 'options' ] = options
          break

    else :
      raise OutputException ()


  def success ( self, 
                message     : str  = "Operación exitosa", 
                data        : dict = None, 
                status_code : int  = 200,
                redir       : dict = None,
                render      : dict = None
              ) :
    # JSON Case / Caso JSON
    if self._wants_json :
      payload = {
        "success" : True,
        "message" : message,
        "data" : self.data ( data or {} )
      }
      return jsonify ( payload ), status_code

    # Caso: redirección explícita
    if redir and redir [ "enabled" ] :
      flash ( message, "success" )
      return redirect ( url_for ( redir [ "target" ], **( redir [ "context" ] or {} ) ))

    # Caso: render_template con contexto
    if render and render [ "enabled" ] :
      html = render_template ( render [ "template" ], **( render [ "context" ] or {} ) )
      return make_response ( html, status_code, SuccessHttp.contentTypeHtml () )

    # Fallback: solo mensaje
    return message, status_code


  def error ( self, _msg : str, _type : str, _status : int ) -> None :
    self._hasError = True
    self._output = {
      'error'  : _msg,
      'type'   : _type, # warning, fatal, error, normal
      'status' : _status #200, 401, ...
    }


  def exception ( self, _msg : str, _type : str, _status : int ) -> None :
    self.error ( _msg, _type, _status )
