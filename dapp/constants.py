import pkgutil
from pathlib import Path

ROOT_DIR = Path(pkgutil.get_loader("dapp").get_filename()).parent
RESOURCES_DIR = ROOT_DIR / "resources"
