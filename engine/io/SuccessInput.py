# Python Libraries / Librerías Python
from flask import request

# Success Libraries / Librerías Success
from success.common.base.SuccessClass    import SuccessClass
from success.common.base.SuccessClass    import abstractmethod
from success.engine.models.SuccessSchema import SuccessSchema
from success.common.tools.SuccessHttp    import SuccessHttp

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessInput ( SuccessClass ) :

  _errors        : list          = []
  _method                        = None
  _rawData       : dict          = None
  _schema        : SuccessSchema = None
  _validatedData : dict          = {}

  
  def __init__ ( self ) -> None :
    super ().__init__ ()
    self._rawData = {}


  def _parseInput ( self ) -> None :
    if SuccessHttp.isGet () :
      self._rawData = request.args.to_dict ()

    elif SuccessHttp.isPost () or SuccessHttp.isPut () or SuccessHttp.isPatch () :
      if request.is_json :
        self._rawData = request.get_json ( silent = True ) or {}

      else :
        self._rawData = request.form.to_dict ()

    elif SuccessHttp.isDelete () :
      self._rawData = request.args.to_dict ()
      if request.is_json :
        self._rawData.update ( request.get_json ( silent = True ) or {} )

    else : 
      self._rawData = {}


  def get ( self, key, default = None ) :
    return self._rawData.get ( key, default )

  
  @abstractmethod
  def parse ( self ) :
    pass

  
  @abstractmethod
  def validate ( self ) :
    pass
