from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(text_widget):
    # Open a file dialog to select a file for opening
    filename = askopenfilename()
    if filename:
        with open(filename, "r") as file:
            content = file.read()
            text_widget.insert("end", content)
def save_file(text_widget):
    # Open a file dialog to select a location for saving the file
    filename = asksaveasfilename()
    if filename:
        with open(filename, "w") as file:
            content = text_widget.get(1.0, "end-1c")  # Get content without trailing newline
            file.write(content)