# Python Libraries / Librerías Python
from colorama import init as colorama_init, Fore, Style

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones



class SuccessColor :

  # Colores base
  PURPLE    = Fore.MAGENTA
  CYAN      = Fore.CYAN
  GREEN     = Fore.GREEN
  YELLOW    = Fore.YELLOW
  RED       = Fore.RED
  BLUE      = Fore.BLUE
  WHITE     = Fore.WHITE
  GRAY      = Fore.LIGHTBLACK_EX

  # Estilos
  BOLD      = Style.BRIGHT
  NORMAL    = Style.NORMAL
  DIM       = Style.DIM
  RESET     = Style.RESET_ALL

  HEADER  = '\033[95m'
  OKBLUE  = '\033[94m'
  OKCYAN  = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL    = '\033[91m'
  WHITE   = '\033[97m'
  GRAY    = '\033[90m'
  ENDC    = '\033[0m'


  @staticmethod
  def decorate ( msg, fg = WHITE, style = NORMAL ) :
    return f"{fg}{style}{msg}{SuccessColor.RESET}"


  @staticmethod
  def methodColor ( method ) :
    color = {
      'GET'    : SuccessColor.OKGREEN,
      'POST'   : SuccessColor.WARNING,
      'PUT'    : SuccessColor.OKBLUE,
      'DELETE' : SuccessColor.FAIL
    }.get ( method.upper (), SuccessColor.WHITE )
    return SuccessColor.decorate ( method, color )


  @staticmethod
  def info ( msg ) :
    return f"{SuccessColor.CYAN}{SuccessColor.BOLD}{msg}{SuccessColor.RESET}"


  @staticmethod
  def warn ( msg ) :
    return f"{SuccessColor.YELLOW}{SuccessColor.BOLD}{msg}{SuccessColor.RESET}"


  @staticmethod
  def error ( msg ) :
    return f"{SuccessColor.RED}{SuccessColor.BOLD}{msg}{SuccessColor.RESET}"


  @staticmethod
  def success ( msg ) :
    return f"{SuccessColor.GREEN}{SuccessColor.BOLD}{msg}{SuccessColor.RESET}"


  @staticmethod
  def level ( msg ) :
    return f"{SuccessColor.WHITE}{msg}{SuccessColor.RESET}"


  @staticmethod
  def tag ( msg ) :
    return f"{SuccessColor.WARNING}{msg}{SuccessColor.RESET}"


  @staticmethod
  def title ( msg ) :
    return f"{SuccessColor.PURPLE}{SuccessColor.BOLD}{msg}{SuccessColor.RESET}"


  @staticmethod
  def subtle ( msg ) :
    return f"{SuccessColor.GRAY}{msg}{SuccessColor.RESET}"
