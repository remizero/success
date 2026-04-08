# Python Libraries / Librerías Python
from enum import Enum

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessHookAuditLevel ( str, Enum ) :
  OFF     = "OFF"
  LENIENT = "LENIENT"
  STRICT  = "STRICT"

# try:
#     level = SuccessHookAuditLevel(audit_level)
# except ValueError:
#     raise RuntimeError(f"Nivel de auditoría de hooks no válido: {audit_level}")
