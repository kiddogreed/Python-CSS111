#author: John RUsselle Domingo
#Date: Oct24_2024=
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("AREA Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()
    
def populate_main_window(frm_main):
    """
    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create labels for width, height, and area.
    lbl_width = Label(frm_main, text="Width (w):")
    lbl_height = Label(frm_main, text="Height (h):")
    lbl_area = Label(frm_main, text="Area (a = w * h):")

    # Create integer entry boxes for width and height.
    ent_width = IntEntry(frm_main, width=12,lower_bound=12, upper_bound=90)
    ent_height = IntEntry(frm_main, width=12,lower_bound=12, upper_bound=90)
  
    # Create a label to display the calculated area.
    lbl_area_result = Label(frm_main, text="")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(row=0, column=0, padx=3, pady=3)
    ent_width.grid(row=0, column=1, padx=3, pady=3)

    lbl_height.grid(row=1, column=0, padx=3, pady=3)
    ent_height.grid(row=1, column=1, padx=3, pady=3)

    lbl_area.grid(row=2, column=0, padx=3, pady=3)
    lbl_area_result.grid(row=2, column=1, padx=3, pady=3)

    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=2, sticky="w")

    # Function to calculate and display the area.
    def calculate(event):
        """Compute and display the area of the rectangle."""
        try:
            width = int(ent_width.get())
            height = int(ent_height.get())
            area = width * height
            lbl_area_result.config(text=f"{area}")
        except ValueError:
            lbl_area_result.config(text="Invalid input")

    # Function to clear all inputs and results.
    def clear():
        """Clear all input fields and the area result."""
        ent_width.delete(0, 'end')
        ent_height.delete(0, 'end')
        lbl_area_result.config(text="")

    # Bind the calculate function to the width and height entry boxes.
    ent_width.bind("<KeyRelease>", calculate)
    ent_height.bind("<KeyRelease>", calculate)
if __name__ == "__main__":
    main()