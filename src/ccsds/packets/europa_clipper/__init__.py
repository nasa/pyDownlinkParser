"""Package file."""
import pkgutil

__all__ = []
for loader, module_name, _ in pkgutil.walk_packages(__path__):
    if "test" not in module_name:
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module
