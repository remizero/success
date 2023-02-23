# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from utils import EnvVar


# Preconditions / Precondiciones


class File () :

  @staticmethod
  def getLastNumberLine () -> int :
    file  = open ( EnvVar.get ( 'LOGGER_DIR' ), 'r' )
    lines = file.readlines ()
    count = len ( lines )
    file.close ()
    return count
