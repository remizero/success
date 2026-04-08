import click
from rich.console import Console
from rich.table import Table

from success.registry import SuccessAppRegistry
from success.config import load_apps_config  # suponiendo que esto lee el YAML o similar

@click.command("apps:list", short_help="Lista todas las aplicaciones registradas en Success")
def list_apps():
    console = Console()
    config = load_apps_config()
    registry = SuccessAppRegistry(config)

    apps = registry._apps
    domain = registry._domain
    subdomains = registry._use_subdomains

    total = len(apps)
    active = 0

    table = Table(title="Success - Apps Registradas")
    table.add_column("Estado", justify="center")
    table.add_column("App")
    table.add_column("Label")
    table.add_column("URL", style="cyan")

    for name, meta in apps.items():
        enabled = meta.get("enabled", True)
        label = meta.get("label", name)
        url = registry.get_url(name) if enabled else "[DESACTIVADA]"

        estado = "✔️" if enabled else "✖️"
        if enabled:
            active += 1

        table.add_row(estado, name, label, url)

    console.print(table)
    console.print(f"Total: {total} apps ({active} activas, {total - active} desactivadas)")
