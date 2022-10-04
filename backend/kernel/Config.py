# Python Libraries / Librerías Python
import os
from dotenv import load_dotenv


# Application Libraries / Librerías de la Aplicación
from kernel.Debug import Debug


# Preconditions / Precondiciones
path = os.path.abspath ( os.getcwdb () )
pathAux = path [ 0 : len ( path ) ]
currentPath = pathAux.decode ( "utf-8" )
load_dotenv ( os.path.join ( currentPath, '.env' ) )


class Config ( object ) :

  def __init__ ( self ) -> None :
    pass
