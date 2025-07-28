import tkinter as tk
from tkinter import ttk

def open_map_screen(root):
    map_win = tk.Toplevel(root)
    map_win.title("Interactive Map")
    tk.Label(map_win, text="Map Screen Placeholder").pack(padx=20, pady=20)