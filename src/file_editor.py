"""
File Editor Module

This module provides a class for a simple text editor using Tkinter.

Classes:
- FileEditor: A class for a simple text editor.
"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from .file_operations import open_file, save_file

class FileEditor:
    """A class for a simple text editor using Tkinter."""

    def __init__(self):
        """Initialize the FileEditor class."""
        # Initialize the Tkinter window
        self.window = Tk()
        self.window.title("Text Editor")

        # Create a menu bar
        menubar = Menu(self.window)
        self.window.config(menu=menubar)  # Display the menu bar

        # Create a File menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

        # Add a tool bar frame
        self.create_toolbar()

        # Add a text editor frame
        self.create_text_editor()

        self.window.mainloop()  # Start the GUI event loop

    def create_toolbar(self):
        """Create and add a frame for the toolbar."""
        # Create and add a frame for the toolbar
        toolbar_frame = Frame(self.window)
        toolbar_frame.grid(row=1, column=1, sticky=W)

        # Load images for buttons
        open_image = PhotoImage(file="image/open-folder.png")
        save_image = PhotoImage(file="image/save.png")

        # Create buttons for opening and saving files
        Button(toolbar_frame, image=open_image, command=self.open_file).grid(row=1, column=1, sticky=W)
        Button(toolbar_frame, image=save_image, command=self.save_file).grid(row=1, column=2)

    def create_text_editor(self):
        """Create a frame for the text editor."""
        # Create a frame for the text editor
        editor_frame = Frame(self.window)
        editor_frame.grid(row=2, column=1)

        # Add a scrollbar to the text editor
        scrollbar = Scrollbar(editor_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Create a Text widget for editing text
        self.text = ScrolledText(editor_frame, width=40, height=20, wrap=WORD, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)

    def open_file(self):
        """Open a file."""
        open_file(self.text)

    def save_file(self):
        """Save a file."""
        save_file(self.text)
