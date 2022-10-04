# Python Libraries / Librerías Python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import render_template
from logging import LogRecord
from logging.handlers import SMTPHandler
from smtplib import (
  SMTP,
  SMTP_SSL,
  SMTPAuthenticationError,
  SMTPDataError,
  SMTPException,
  SMTPHeloError,
  SMTPNotSupportedError,
  SMTPRecipientsRefused,
  SMTPSenderRefused
)
import ssl


# Application Libraries / Librerías de la Aplicación
from kernel import Debug
from utils import EnvVar


# Preconditions / Precondiciones


class LoggerMailer ( SMTPHandler ) :

  __stmp : SMTP or SMTP_SSL = None

  def __init__( self ) -> None :
    config = {
      'mailhost' : EnvVar.get ( 'LOGGER_MAIL_SERVER' ),
      'fromaddr' : EnvVar.get ( 'LOGGER_MAIL_USERNAME' ),
      'toaddrs' : EnvVar.get ( 'LOGGER_MAIL_PASSWORD' ),
      'subject' : EnvVar.get ( 'LOGGER_MESSAGE_SUBJECT' )
    }
    super ().__init__ ( **config )
    self.mailport = EnvVar.get ( 'LOGGER_MAIL_PORT' )
    if ( EnvVar.isTrue ( 'LOGGER_MAIL_SSL' ) ) :
      
      self.__smtp = SMTP_SSL ()

    else :

      self.__smtp = SMTP ()

  def emit ( self, record : LogRecord ) -> None :

    try :

      self.__smtp.connect ( host = self.mailhost, port = self.mailport )
      if ( not EnvVar.isTrue ( 'LOGGER_MAIL_SSL' ) ) :
        self.__smtp.ehlo ()
        # Create a secure SSL context
        # context = ssl.create_default_context ()
        # self.__smtp.starttls ( context = context )
        self.__smtp.starttls ( *self.secure )
        self.__smtp.ehlo ()
      self.__smtp.login ( user = self.fromaddr, password = self.password )
      email = MIMEMultipart ( 'alternative' )
      email.set_charset ( 'utf-8' )
      email [ 'Subject' ] = EnvVar.get ( 'LOGGER_MESSAGE_SUBJECT' )
      email [ 'From' ] = self.fromaddr
      email [ 'To' ] = EnvVar.get ( 'LOGGER_ADMIN' )
      # TODO Falta procesar el objeto exc_info del objeto record para resaltar
      # la informacion mas importante.
      # https://docs.python.org/3/library/logging.html#logrecord-objects
      template = ''
      if ( isinstance ( record.exc_info, Exception ) ) :
        template = EnvVar.get ( 'LOGGER_TEMPLATE_HTML_EXCEPTION' )
      else :
        template = EnvVar.get ( 'LOGGER_TEMPLATE_HTML_ERROR' )
      Debug.log ( record.exc_info )
      payload = MIMEText ( render_template ( template, **record.exc_info ), 'html' )
      email.attach ( payload )
      self.__smtp.sendmail ( msg = email.as_string (), from_addr = self.fromaddr, to_addrs = EnvVar.get ( 'LOGGER_ADMIN' ) )

    except (
      RuntimeError,
      SMTPAuthenticationError,
      SMTPDataError,
      SMTPException,
      SMTPHeloError,
      SMTPNotSupportedError,
      SMTPRecipientsRefused,
      SMTPSenderRefused
    ) as exception :
      # TODO como procesar estas excepciones
      self.handleError ( record )
    
    except :

      self.handleError ( record )

    finally :

      self.__smtp.quit ()
