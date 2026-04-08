# Python Libraries / Librerías Python
from flask                 import json
from flask                 import request
from flask                 import Response
from flask_restful         import Resource
from http                  import HTTPStatus
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

# Success Libraries / Librerías Success
from success.core.SuccessContext                      import SuccessContext
from success.common.exceptions.JsonRequestException   import JsonRequestException
from success.common.exceptions.LoginException         import LoginException
from success.common.exceptions.OutputException        import OutputException
from success.common.exceptions.RequestMethodException import RequestMethodException
from success.common.infra.logger.SuccessLogger        import SuccessLogger
from success.common.SuccessDebug                      import SuccessDebug
from success.common.base.SuccessClass                 import SuccessClass
from success.engine.context.helpers.Context           import Context
from success.engine.io.SuccessOutput                  import SuccessOutput
from success.engine.models.SuccessPermissions         import SuccessPermissions
from success.engine.models.SuccessSession             import SuccessSession
from success.common.tools.SuccessEncryption           import SuccessEncryption
from success.common.tools.SuccessHttp                 import SuccessHttp
from success.common.tools.SuccessResultset            import SuccessResultset
from success.common.tools.SuccessStructs              import SuccessStructs
from success.engine.infrastructure.SuccessController  import SuccessController
from success.engine.io.SuccessInput                   import SuccessInput

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones
jwt = SuccessContext ().getExtension ( "SuccessJwtExtension" )
if jwt is None :
  raise RuntimeError ( "La extensión SuccessJwtExtension no está cargada" )


class SuccessAction ( SuccessClass ) :

  _context    : str               = 'json'
  _controller : SuccessController = None
  _input      : SuccessInput      = None
  _inputData  : dict              = None
  _output     : SuccessOutput     = None
  _response   : Response          = None
  _status     : HTTPStatus        = HTTPStatus.BAD_REQUEST


  def __init__( self, _input : SuccessInput, _output : SuccessOutput, _controller : SuccessController ) -> None :
    super ().__init__ ()
    self._input      = _input
    self._output     = _output
    self._controller = _controller


    self._context = Context ().resolve ( request )

    if ( SuccessHttp.isMethod ( 'POST' ) and self._context == 'json' ) :
      try :
        self._inputData = self._input.load ( request.get_json () )

      except ( ValidationError, SchemaError ) as e :
        raise JsonRequestException ( str ( e ) )
