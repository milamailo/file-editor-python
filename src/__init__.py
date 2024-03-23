"""
Initialization module for the 'src' package.

Defines the list of modules to be imported when the package is imported.

Modules:
- file_editor: Contains the FileEditor class for the text editor.
- file_operations: Contains functions for opening and saving files.
"""

# Define the list of modules to be imported when the package is imported
__all__ = ['file_editor', 'file_operations']

# Import modules to make them available when the package is imported
from . import file_editor
from . import file_operations
