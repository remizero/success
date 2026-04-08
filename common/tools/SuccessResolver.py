from pathlib import Path
import importlib
from typing import List, Type, Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class DiscoveredModule:
    fs_path: Path
    import_path: str
    is_package: bool

class SuccessResolver:
  """
  Unifica funcionalidades de SuccessPathResolver y ModuleResolver
  para descubrimiento de paths, resolución semántica y carga dinámica.
  """

  def __init__(self, root: Path):
    self.root = root

  # -------------------------------
  # 1️⃣ Discovery (filesystem)
  # -------------------------------
  def discover_paths(self, subdir: Optional[str] = None) -> List[DiscoveredModule]:
    """
    Descubre módulos y paquetes en el filesystem
    sin importar nada en runtime.
    """
    base = self.root / subdir if subdir else self.root
    modules = []

    for path in base.rglob("*.py"):
      if path.name == "__init__.py":
        is_pkg = True
      else:
        is_pkg = False

      # calcular import path relativo
      import_path = ".".join(path.relative_to(self.root).with_suffix("").parts)
      modules.append(DiscoveredModule(fs_path=path, import_path=import_path, is_package=is_pkg))

    return modules

  # -------------------------------
  # 2️⃣ Semantic resolution
  # -------------------------------
  def resolve_blueprint_name(self, fs_path: Path) -> str:
    """
    Devuelve el nombre semántico del blueprint basado
    en la estructura de directorios de Success.
    """
    parts = fs_path.relative_to(self.root).parts
    return "_".join(parts[:-1])  # ejemplo: apps_synthetos_services_view_chromadb

  def resolve_subdomain(self, fs_path: Path) -> str:
    """
    Determina el subdomain a usar para Flask, con fallback al .env
    """
    from os import getenv
    return getenv("SUCCESS_SUBDOMAIN", fs_path.parts[1])

  def resolve_endpoint_rule(self, fs_path: Path) -> str:
    """
    Devuelve la regla de endpoint a partir del nombre de acción
    """
    return f"/{fs_path.stem}"

  # -------------------------------
  # 3️⃣ Runtime imports
  # -------------------------------
  def import_module(self, import_path: str):
    """
    Importa el módulo de Python en runtime
    """
    return importlib.import_module(import_path)

  def load_class(self, import_path: str, class_name: str) -> Type:
    """
    Devuelve la clase de un módulo
    """
    module = self.import_module(import_path)
    return getattr(module, class_name)
