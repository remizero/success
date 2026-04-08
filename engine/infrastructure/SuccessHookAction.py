# Python Libraries / Librerías Python
from enum import Enum

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessHookAction ( str, Enum ) :
  
  CONTEXT_INJECTION  = "context_injection"
  CONFIG_EXTEND      = "config_extend"
  BOOTSTRAP_READY    = "bootstrap_ready"
  CUSTOM_EXTENSION   = "custom_extension"
  BLUEPRINT_REGISTER = "blueprint_register"
  MIDDLEWARE_ATTACH  = "middleware_attach"
  SERVICE_DISCOVERY  = "service_discovery"
  SIMULATOR_SETUP    = "simulator_setup"
  LOGGER_ATTACH      = "logger_attach"
  # Puedes ir agregando más acciones válidas aquí
