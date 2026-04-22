# Python Libraries / Librerías Python
from enum import Enum

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessDispatchMode ( str, Enum ) :
  """
  Dispatch mode enumeration for multiApp applications.

  Defines available modes for application routing
  in the Success system.

  Available modes:
  ------------------
  - SUBDOMAIN: Dispatch based on subdomains (app1.domain.com)
  - PATH: Dispatch based on route prefixes (/app1, /app2)
  - STANDARD: Standard dispatch with DispatcherMiddleware

  Usage:
  ------
  # Check mode
  if mode == SuccessDispatchMode.SUBDOMAIN:
      # Configure subdomain dispatch
      pass

  # Compare with string
  mode = SuccessDispatchMode("subdomain")
  mode == "subdomain"  # True

  Note:
    - Mode is configured via SUCCESS_APP_MODE
    - Each mode requires specific Flask configuration
  """
  SUBDOMAIN = "subdomain"
  PATH      = "path"
  STANDARD  = "standard"
