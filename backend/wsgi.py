# Python Libraries / Librerías Python
import os
import sys


# Application Libraries / Librerías de la Aplicación
from kernel import success


# Preconditions / Precondiciones
PROJECT_ROOT = os.path.abspath ( 
  os.path.join (
    os.path.dirname ( __file__ ),
    os.pardir
  )
)
sys.path.append ( PROJECT_ROOT )


successApp = success.getApp ()

if __name__ == "__main__" :
  successApp.run ()
