from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(text_widget):
    # Open a file dialog to select a file for opening
    filename = askopenfilename()
    if filename:
        with open(filename, "r") as file:
            content = file.read()
            text_widget.insert("end", content)