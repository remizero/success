# Python Libraries / Librerías Python
from dotenv import load_dotenv
import os


# Application Libraries / Librerías de la Aplicación
from kernel import Debug
from utils  import EnvVar


# Preconditions / Precondiciones
path        = os.path.abspath ( os.getcwdb () )
pathAux     = path [ 0 : len ( path ) ]
currentPath = pathAux.decode ( "utf-8" )
load_dotenv ( os.path.join ( currentPath, '.env' ) )



class Config ( object ) :

  def __init__ ( self ) -> None :
    pass
