"""
Employee Management System Module

This module provides various functionalities for managing employee data.
"""

# Define the list of modules to be imported when the package is imported
# This list specifies the modules that will be imported when using "from package import *"
# In this case, only the file_editor module is exposed to the user
__all__ = ['file_editor']

# Import the file_editor module from the src subpackage
# This import statement allows the file_editor functions to be accessed directly from the package
# Users can use "from package import file_editor" to access the file_editor functions
from .src import file_editor
