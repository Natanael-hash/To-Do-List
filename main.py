import tkinter as tk
from src.gui import TaskManagerGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()