try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # Python < 3.8
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version("PyTrilium")
except PackageNotFoundError:
    # Package is not installed, likely in development
    __version__ = "dev"