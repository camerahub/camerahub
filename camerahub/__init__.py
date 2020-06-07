import poetry_version

# Extract version from poetry pyproject.toml file
__version__ = poetry_version.extract(source_file=__file__)
