# Python Libraries / Librerías Python
from flask      import Flask
from flask      import render_template
from flask_mail import Mail
from flask_mail import Message
from typing     import Any
import os

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessExtension import SuccessExtension
from success.common.tools.SuccessEnv      import SuccessEnv

# Preconditions / Precondiciones


class SuccessEmailExtension ( SuccessExtension ) :

  __message = Message


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    self._extension = Mail ()


  def message ( self,
      _subject       : str         = '',
      _body          : str         = None,
      _html          : str         = None,
      _sender        : str         = None,
      _cc            : str or list = None,
      _bcc           : str or list = None,
      _attachments   : Any         = None,
      _reply_to      : Any         = None,
      _date          : Any         = None,
      _charset       : str         = 'utf-8',
      _extra_headers : Any         = None,
      _mail_options  : Any         = None,
      _rcpt_options  : Any         = None,
      _template      : str         = None,
      **context      : dict [ str, Any ]
    ) -> None :

    # TODO VALIDAR TODOS LOS PARAMETROS
    # TODO MANEJO DE ARCHIVOS ADJUNTOS
    if ( _sender is None ) :
      if ( os.environ.get ( 'MAIL_DEFAULT_SENDER' ) != '' ) :
        _sender = os.environ.get ( 'MAIL_DEFAULT_SENDER' )
      else :
        _sender = os.environ.get ( 'MAIL_DEFAULT_SENDER' )
    self.__message = Message (
      subject       = _subject,
      body          = _body,
      html          = _html,
      sender        = _sender,
      cc            = _cc,
      bcc           = _bcc,
      attachments   = _attachments,
      reply_to      = _reply_to,
      date          = _date,
      charset       = _charset,
      extra_headers = _extra_headers,
      mail_options  = _mail_options,
      rcpt_options  = _rcpt_options
    )
    if ( _body != None ) :
      self.__message.body = _body
    if ( _template != None ) :
      self.__message.html = render_template ( _template, **context )


  def send ( self, _receiver : str ) :
    self.__message.add_recipient ( _receiver )
    self._extension.send ( self.__message )


  def sendMultiple ( self, _receiver : list = None ) -> None :
    with self._extension.connect () as connection :
      for receiver in _receiver :
        self.__message.add_recipient ( receiver )
        connection.send ( self.__message )
