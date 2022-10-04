# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones
# https://www.peterspython.com/es/blog/cree-sus-propias-clases-de-excepcion-python-personalizadas-y-adaptadas-a-su-aplicacion
# https://www.delftstack.com/es/howto/python/python-custom-exception/
# https://www.delftstack.com/es/howto/python/print-an-exception-in-python/
# https://www.kite.com/python/answers/how-to-log-an-exception-with-traceback-in-python
# https://programmer.help/blogs/using-logging-and-traceback-modules-to-log-and-trace-exceptions-in-python.html
# https://www.loggly.com/blog/exceptional-logging-of-exceptions-in-python/
# https://www.delftstack.com/howto/python/python-print-stack-trace/
# https://gankrin.org/how-to-log-an-error-in-python/
# https://www.pythonpool.com/python-traceback/


class Exception ( Exception ) :

  def __init__ ( self, e = None, code = None, message = None, details = None, fargs = None ) :
    self.e = e
    self.code = code
    self.message = message
    self.details = details
    self.fargs = fargs

  def getE ( self ) :
    return self.e

  def getCode ( self ) :
    return self.code

  def getMessage ( self ) :
    return self.message

  def getDetails ( self ) :
    return self.details

  def __str__ ( self ) :
    s_items = []
    if self.e is not  None:
      s_items.append ( 'e = {}'.format ( self.e ) )
    if self.code is not  None:
      s_items.append ( 'code = {}'.format ( self.code ) )
    if self.message is not  None:
      s_items.append ( 'message = {}'.format ( self.message ) )
    if self.details is not  None:
      s_items.append ( 'details = {}'.format ( self.details ) )
    if self.fargs is not  None:
      s_items.append ( 'fargs = {}'.format ( self.fargs ) )
    return ', '.join ( s_items )
